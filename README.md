python-inotify
==============

About python-inotify
--------------------

This is python-inotify, a Python interface to the Linux 2.6 kernel's
inotify subsystem.  The inotify subsystem provides an efficient way to
let a process watch for changes to files and directories.

This package provides both low- and high-level interfaces to inotify.

The low-level interface is provided through the inotify module.  It
provides wrappers around the inotify system calls, a read function
that returns useful event objects, and relevant constants.

The higher-level interface is more useful, and is provided through the
inotify.watcher package.  It provides two classes, Watcher and
AutoWatcher, which allow you to not worry about file descriptor
management, and a third, Threshold, which lets you decide whether you
want to read queued events yet.



This package is *not* pyinotify
-------------------------------

To confuse matters a little, there's another Python inotify interface
available, called pyinotify.  I wrote python-inotify as a reaction to
pyinotify, after trying to use pyinotify a little and finding it
lacking.  In my admittedly brief experience, pyinotify was buggy and
slow to the extent that I stopped trying to fix its problems and wrote
a new implementation instead.

One difference is that pyinotify has a callback based API in which you 
define callbacks or methods that are called when a specific event happens, 
forcing an event-driven programmig style. Python-inotify has an API that 
allows you to use a blocking `Watcher.read()` call. 

You can find pyinotify at http://pyinotify.sourceforge.net/

Build
-----

`python -m build`

Notice of copyright and license
-------------------------------

This library is free software; you can redistribute it and/or modify
it under the terms of version 2.1 of the GNU Lesser General Public
License as published by the Free Software Foundation.

This library is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library, in the file named COPYING; if not,
write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth
Floor, Boston, MA 02110-1301 USA
