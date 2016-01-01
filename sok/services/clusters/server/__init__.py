"""
This package provides an HTTP server for access to resources in local repository.
"""
import falcon
from .product import ProductResource
from .environment import EnvResource

application = falcon.API()

application.add_route('/registry/product', ProductResource())
application.add_route('/registry/environment', EnvResource())
