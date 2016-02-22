import falcon
import json


class ProductHandler(object):

    def __init__(self, manager):
        self._manager = manager

    def on_get(self, req, resp, uid):
        product = self._manager.get()
        resp.body = json.dumps(product)
        resp.status = falcon.HTTP_200

