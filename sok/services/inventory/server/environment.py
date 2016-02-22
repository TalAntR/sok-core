

class EnvHandler(object):

    def __init__(self, manager):
        self._manager = manager

    def on_get(self, req, resp, uid):
        product = self._manager.get(uid)
        resp.body = json.dumps(product)
        resp.status = falcon.HTTP_200


