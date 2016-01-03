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
from .product import ProductResource
from .environment import EnvResource

application = falcon.API()

application.add_route('/registry/product', ProductResource())
application.add_route('/registry/environment', EnvResource())
