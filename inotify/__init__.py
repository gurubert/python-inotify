# __init__.py - low-level interfaces to the Linux inotify subsystem

# Copyright 2006 Bryan O'Sullivan <bos@serpentine.com>
# Copyright 2012-2013 Jan Kanis <jan.code@jankanis.nl>

# This library is free software; you can redistribute it and/or modify
# it under the terms of version 2.1 of the GNU Lesser General Public
# License, incorporated herein by reference.

# Additionally, code written by Jan Kanis may also be redistributed and/or 
# modified under the terms of any version of the GNU Lesser General Public 
# License greater than 2.1. 

'''
Low-level interface to the Linux inotify subsystem.

The inotify subsystem provides an efficient mechanism for file status
monitoring and change notification.

This package provides the low-level inotify system call interface and
associated constants and helper functions.

For a higher-level interface that remains highly efficient, use the
inotify.watcher package.
'''

__author__ = "Jan Kanis <jan.code@jankanis.nl>"

from ._inotify import *

procfs_path = '/proc/sys/fs/inotify'

def _read_procfs_value(name):
    def read_value():
        try:
            return int(open(procfs_path + '/' + name).read())
        except OSError as err:
            return None

    read_value.__doc__ = '''Return the value of the %s setting from /proc.

    If inotify is not enabled on this system, return None.''' % name

    return read_value

max_queued_events = _read_procfs_value('max_queued_events')
max_user_instances = _read_procfs_value('max_user_instances')
max_user_watches = _read_procfs_value('max_user_watches')
