# A somewhat more performant example of how to use the inotify
# subsystem.

# In this example, we delay reading from the inotify file descriptor
# until either it has enough events queued to be worth reading, or a
# timeout passes.

# This greatly reduces the number of read() system calls we issue when
# monitoring a busy filesystem, and substantially reduces CPU
# overhead.  This also has the nice feature of delaying work for a few
# moments, which will in many cases put it off until the system would
# otherwise be idle.

from __future__ import print_function

from inotify import watcher
import inotify
import select
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

poll = select.poll()
poll.register(w, select.POLLIN)

timeout = None

threshold = watcher.Threshold(w, 512)

while True:
    events = poll.poll(timeout)
    nread = 0
    if threshold() or not events:
        print('reading,', threshold.readable(), 'bytes available')
        for evt in w.read(0):
            nread += 1

            # The last thing to do to improve efficiency here would be
            # to coalesce similar events before passing them up to a
            # higher level.

            # For example, it's overwhelmingly common to have a stream
            # of inotify events contain a creation, followed by
            # multiple modifications of the created file.

            # Recognising this pattern (and others) and coalescing
            # these events into a single creation event would reduce
            # the number of trips into our app's presumably more
            # computationally expensive upper layers.

            print(repr(evt.fullpath), ' | '.join(inotify.decode_mask(evt.mask)))
    if nread:
        print('plugging back in')
        timeout = None
        poll.register(w, select.POLLIN)
    else:
        print('unplugging,', threshold.readable(), 'bytes available')
        timeout = 1000
        poll.unregister(w)
