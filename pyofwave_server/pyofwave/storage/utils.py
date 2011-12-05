import os
from importlib import import_module
import logging

from pyofwave.conf.exception import ConfigurationError

logger = logging.getLogger("pyofwave.server")

def load_backend(backend_name):
    # Lookup and load the module
    try:
        module = import_module(backend_name)
    except ImportError, e:
        backend_dir = os.path.join(os.path.dirname(__file__), 'backends')

        # Display available backends if this one wasn't found
        try:
            available_backends = [f.rstrip('.py') for f in os.listdir(backend_dir)
                                  if not f.startswith('.')
                                  and not f.startswith('__')
                                  ]
        except EnvironmentError:
            available_backends = []

        raise ConfigurationError("The backend '%s' couldn't be found.\nAvailable built-in backends: %s" % (backend_name,
                                                                                                           available_backends)
                                 )
    
    
    # Instanciate the backend
    datastorage =  module.DataStorage()
    logger.info("Loaded datastore backend '%s'." % backend_name)
    return datastorage

            
