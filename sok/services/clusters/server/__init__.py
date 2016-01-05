"""
This package provides an HTTP server for access to resources in local
repository. It's embedded implementation of the Cluster API which might be used
by default after installation.

It's supposed that definitions for all products and its resources are described
in YAML files in a special folder on local disk. Please, look at *product*
directory in the root of this project.

The current implementation uses the Falcon web framework
"""
import falcon
from .manager import HandlerFactory

handlers = HandlerFactory()
application = falcon.API()

application.add_route('/registry/product/{uid}', handlers.get_product_handler())
application.add_route('/registry/environment', handlers.get_environment_handler())
