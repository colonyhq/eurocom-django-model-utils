import uuid

from django.core.serializers.json import DjangoJSONEncoder


class EDMUJSONEncoder(DjangoJSONEncoder):
    """
    JSONEncoder subclass that knows how to encode date/time, decimal and UUID types.
    """
    def default(self, o):
        if isinstance(o, uuid.UUID):
            return str(o)
        else:
            return super(EDMUJSONEncoder, self).default(o)