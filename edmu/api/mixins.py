from rest_framework import mixins
from rest_framework.views import APIView


class MethodPermissionCheckAPIView(APIView):
    """
    Adds extra methods to the ``GenericAPIView`` class to handle the getting and checking of method permissons.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        method = self.request.method.lower()

        try:
            use_permission_classes = getattr(self, '%s_permission_classes' % method)
        except AttributeError:
            use_permission_classes = self.permission_classes

        return [permission() for permission in use_permission_classes]


class CreateAPIView(mixins.CreateModelMixin,
                    MethodPermissionCheckAPIView):
    """
    Concrete view for listing a model instance.
    """
    allowed_methods = ['post', ]


class ListAPIView(mixins.ListModelMixin,
                  MethodPermissionCheckAPIView):
    """
    Concrete view for listing a model instance.
    """
    allowed_methods = ['get', ]


class RetrieveAPIView(mixins.CreateModelMixin,
                      MethodPermissionCheckAPIView):
    """
    Concrete view for listing a model instance.
    """
    allowed_methods = ['get', ]


class UpdateAPIView(mixins.UpdateModelMixin,
                    MethodPermissionCheckAPIView):
    """
    Concrete view for listing a model instance.
    """
    allowed_methods = ['put', ]


class DestroyAPIView(mixins.DestroyModelMixin,
                     MethodPermissionCheckAPIView):
    """
    Concrete view for listing a model instance.
    """
    allowed_methods = ['delete', ]


class ListCreateAPIView(mixins.RetrieveModelMixin,
                        MethodPermissionCheckAPIView):
    """
    Concrete view for creating, retrieving or listing a model instance.
    """
    allowed_methods = ['get', 'post']


class RetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin,
                                   MethodPermissionCheckAPIView):
    """
    Concrete view for retrieving, updating or destroying a model instance.
    """
    allowed_methods = ['get', 'put', 'delete']


class RetrieveUpdateAPIView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            MethodPermissionCheckAPIView):
    """
    Concrete view for retrieving or updating a model instance.
    """
    allowed_methods = ['get', 'put']


class RetrieveDestroyAPIView(mixins.RetrieveModelMixin,
                             mixins.DestroyModelMixin,
                             MethodPermissionCheckAPIView):
    """
    Concrete view for retrieving or destroying a model instance.
    """
    allowed_methods = ['get', 'delete']


class UpdateDestroyAPIView(mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           MethodPermissionCheckAPIView):
    """
    Concrete view for retrieving or destroying a model instance.
    """
    allowed_methods = ['put', 'delete']