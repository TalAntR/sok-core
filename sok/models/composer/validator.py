
class AttributeValidator(object):

    def __init__(self, schema):
        self._schema = schema

    def validate(self, attributes):
        resutls = map(self._validate_one, attributes)

    def _validate_one(self, a):
        return False

