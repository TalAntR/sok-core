
class ProductResource(object):

    def on_get(self, req, resp):
        print('Hey: ' + req)

