"""Patches that are applied at runtime to the virtual environment."""

import os
import sys

VIRTUALENV_PATCH_FILE = os.path.join(__file__)


def patch_dist(dist):
    """
    Distutils allows user to configure some arguments via a configuration file:
    https://docs.python.org/3.11/install/index.html#distutils-configuration-files.

    Some of this arguments though don't make sense in context of the virtual environment files, let's fix them up.
    """  # noqa: D205
    # we cannot allow some install config as that would get packages installed outside of the virtual environment
    old_parse_config_files = dist.Distribution.parse_config_files

    def parse_config_files(self, *args, **kwargs):
        result = old_parse_config_files(self, *args, **kwargs)
        install = self.get_option_dict("install")

        if "prefix" in install:  # the prefix governs where to install the libraries
            install["prefix"] = VIRTUALENV_PATCH_FILE, os.path.abspath(sys.prefix)
        for base in ("purelib", "platlib", "headers", "scripts", "data"):
            key = f"install_{base}"
            if key in install:  # do not allow global configs to hijack venv paths
                install.pop(key, None)
        return result

    dist.Distribution.parse_config_files = parse_config_files


# Import hook that patches some modules to ignore configuration values that break package installation in case
# of virtual environments.
_DISTUTILS_PATCH = "distutils.dist", "setuptools.dist"
# https://docs.python.org/3/library/importlib.html#setting-up-an-importer


class _Finder:
    """A meta path finder that allows patching the imported distutils modules."""

    fullname = None

    # lock[0] is threading.Lock(), but initialized lazily to avoid importing threading very early at startup,
    # because there are gevent-based applications that need to be first to import threading by themselves.
    # See https://github.com/pypa/virtualenv/issues/1895 for details.
    lock = []  # noqa: RUF012

    def find_spec(self, fullname, path, target=None):  # noqa: ARG002
... (truncated for brevity)