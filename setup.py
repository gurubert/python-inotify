from setuptools import setup, Extension

setup_args = dict(
    ext_modules = [
        Extension(
            'inotify._inotify',
            ['inotify/_inotify.c'],
            py_limited_api = True
        )
    ]
)
setup(**setup_args)
