from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedModelSerializerOptions


class HyperlinkedNamespaceModelSerializerOptions(HyperlinkedModelSerializerOptions):
    """
    Options for HyperlinkedNamespaceModelSerializer
    """
    def __init__(self, meta):
        super(HyperlinkedNamespaceModelSerializerOptions, self).__init__(meta)
        self.view_name = getattr(meta, 'view_name', None)
        self.view_namespace = getattr(meta, 'view_namespace', None)


class HyperlinkedNamespaceModelSerializer(HyperlinkedModelSerializer):
    """
    A subclass of HyperlinkedModelSerializer that uses hyperlinked relationships using namespaces
    """
    _options_class = HyperlinkedNamespaceModelSerializerOptions

    def __init__(self, *args, **kwargs):
        super(HyperlinkedModelSerializer, self).__init__(*args, **kwargs)
        if self.opts.view_name is None:
            self.opts.view_name = self._get_default_view_name(self.opts.model)

    def _get_default_view_name(self, model):
        view_name = super(HyperlinkedNamespaceModelSerializer, self)._get_default_view_name(model)
        return '%s:%s' % (self.opts.view_namespace, view_name)