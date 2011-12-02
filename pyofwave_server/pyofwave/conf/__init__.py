"""
Settings and configuration for PyOfWave.

Based on the "Django" project (http://django-project.com). Under BSD Licence.

Values will be read from the module specified by the PYOFWAVE_SETTINGS_MODULE environment
variable, and then from pyofwave.conf.global_settings; see the global settings file for
a list of all possible variables.
"""

import importlib
import os
import re
import sys
import time     # Needed for Windows
import warnings

from pyofwave.conf import global_settings
from pyofwave.utils.lazy import LazyObject

ENVIRONMENT_VARIABLE = "PYOFWAVE_SETTINGS_MODULE"

def setup_environ(settings_mod, original_settings_path=None):
    """
    Configures the runtime environment.
    Returns the project directory (assuming the passed settings module is
    directly in the project directory).

    The "original_settings_path" parameter is optional, but recommended, since
    trying to work out the original path from the module can be problematic.
    """
    # Add this project to sys.path so that it's importable in the conventional
    # way. For example, if this file (pyofwave_server) lives in a directory
    # "myproject", this code would add "/path/to/myproject" to sys.path.
    if '__init__.py' in settings_mod.__file__:
        p = os.path.dirname(settings_mod.__file__)
    else:
        p = settings_mod.__file__

    project_directory, settings_filename = os.path.split(p)
    if project_directory == os.curdir or not project_directory:
        project_directory = os.getcwd()
    project_name = os.path.basename(project_directory)
    
    # Strip filename suffix to get the module name.
    settings_name = os.path.splitext(settings_filename)[0]
    
    # Set PYOFWAVE_SETTINGS_MODULE appropriately.
    if original_settings_path:
        os.environ[ENVIRONMENT_VARIABLE] = original_settings_path
    else:
        os.environ[ENVIRONMENT_VARIABLE] = '%s' % (settings_name)

    return project_directory


class POWSettings(LazyObject):
    """
    A lazy proxy for either global PyOfWave settings or a custom settings object.
    The user can manually configure settings prior to using them. Otherwise,
    PyOfWave uses the settings module pointed to by PYOFWAVE_SETTINGS_MODULE.
    """
    def _setup(self):
        """
        Load the settings module pointed to by the environment variable. This
        is used the first time we need any settings at all, if the user has not
        previously configured the settings manually.
        """
        try:
            settings_module = os.environ[ENVIRONMENT_VARIABLE]
            if not settings_module: # If it's set but is an empty string.
                raise KeyError
        except KeyError:
            # NOTE: This is arguably an EnvironmentError, but that causes
            # problems with Python's interactive help.
            raise ImportError("Settings cannot be imported, because environment variable %s is undefined." % ENVIRONMENT_VARIABLE)

        self._wrapped = Settings(settings_module)

    def configure(self, default_settings=global_settings, **options):
        """
        Called to manually configure the settings. The 'default_settings'
        parameter sets where to retrieve any unspecified values from (its
        argument must support attribute access (__getattr__)).
        """
        if self._wrapped != None:
            raise RuntimeError('Settings already configured.')
        holder = UserSettingsHolder(default_settings)
        for name, value in options.items():
            setattr(holder, name, value)
        self._wrapped = holder

    def configured(self):
        """
        Returns True if the settings have already been configured.
        """
        return bool(self._wrapped)
    configured = property(configured)


class Settings(object):
    def __init__(self, settings_module):
        # update this dict from global settings (but only for ALL_CAPS settings)
        for setting in dir(global_settings):
            if setting == setting.upper():
                setattr(self, setting, getattr(global_settings, setting))

        # store the settings module in case someone later cares
        self.SETTINGS_MODULE = settings_module

        try:
            mod = importlib.import_module(self.SETTINGS_MODULE)
        except ImportError, e:
            raise ImportError("Could not import settings '%s' (Is it on sys.path?): %s" % (self.SETTINGS_MODULE, e))

        # Settings are configured, so we can set up the logger if required
        if self.LOGGING_CONFIG:
            # First find the logging configuration function ...
            logging_config_path, logging_config_func_name = self.LOGGING_CONFIG.rsplit('.', 1)
            logging_config_module = importlib.import_module(logging_config_path)
            logging_config_func = getattr(logging_config_module, logging_config_func_name)

            # ... then invoke it with the logging settings
            logging_config_func(self.LOGGING)


class UserSettingsHolder(object):
    """
    Holder for user configured settings.
    """
    # SETTINGS_MODULE doesn't make much sense in the manually configured
    # (standalone) case.
    SETTINGS_MODULE = None

    def __init__(self, default_settings):
        """
        Requests for configuration variables not in this class are satisfied
        from the module specified in default_settings (if possible).
        """
        self.default_settings = default_settings

    def __getattr__(self, name):
        return getattr(self.default_settings, name)

    def __dir__(self):
        return self.__dict__.keys() + dir(self.default_settings)

    # For Python < 2.6:
    __members__ = property(lambda self: self.__dir__())

settings = POWSettings()

