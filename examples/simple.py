# A very simple example of how to use the inotify subsystem.

# I do not recommend following this example in practice, as it has
# fairly considerable CPU overhead.

from __future__ import print_function

from inotify import watcher
import inotify
import sys

w = watcher.AutoWatcher()

paths = sys.argv[1:] or ['/tmp']

for path in paths:
    try:
        # Watch all paths recursively, and all events on them.
        w.add_all(path, inotify.IN_ALL_EVENTS)
    except OSError as err:
        print('%s: %s' % (err.filename, err.strerror), file=sys.stderr)

# If we have nothing to watch, don't go into the read loop, or we'll
# sit there forever.

if not len(w):
    sys.exit(1)

try:
    while True:
        # The Watcher.read method returns a list of event objects.
        for evt in w.read():
            # The inotify.decode_mask function returns a list of the
            # names of the bits set in an event's mask.  This is very
            # handy for debugging.
            print(repr(evt.fullpath), ' | '.join(inotify.decode_mask(evt.mask)))
except KeyboardInterrupt:
    print('interrupted!', file=sys.stderr)
