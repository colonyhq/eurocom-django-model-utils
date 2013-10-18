from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.settings import api_settings


class MethodPermissionCheckAPIView(GenericAPIView):
    """
    Adds extra methods to the ``GenericAPIView`` class to handle the getting and checking of method permissons.
    """
    def get_method_permissions(self, permission_classes):
        """
        Instantiates and returns the list of permissions that the calling method requires.

        :param permission_classes:
            A list of permission classes to instantiate.

        :return:
            A list of instantiated permission classes.
        """
        return [permission() for permission in permission_classes]

    def check_method_permissions(self, permission_classes, request):
        """
        Check if the request should be permitted. Raises an appropriate exception if the request is not permitted.

        :param permission_classes:
            A list of permission classes to check against.
        """
        for permission in self.get_method_permissions(permission_classes):
            if not permission.has_permission(request, self):
                self.permission_denied(request)


class ObjectPermissionCheckMixin(GenericAPIView):
    """
    Mixin to add methods tohandle the getting and checking of object permissons.
    """
    def check_object_permissions(self, permission_classes, request, obj):
        """
        Check if the request should be permitted for a given object.
        Raises an appropriate exception if the request is not permitted.
        """
        for permission in permission_classes:
            if not permission.has_object_permission(request, self, obj):
                self.permission_denied(request)


class ListCreateAPIView(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        MethodPermissionCheckAPIView):
    """
    Concrete view for creating, retrieving or listing a model instance.
    """
    get_permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES
    post_permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES

    def get(self, request, *args, **kwargs):
        self.check_method_permissions(self.get_permission_classes, request)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.check_method_permissions(self.post_permission_classes, request)
        return self.create(request, *args, **kwargs)


class RetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin,
                                   MethodPermissionCheckAPIView):
    """
    Concrete view for retrieving, updating or destroying a model instance.
    """
    retrieve_permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES
    update_permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES
    destroy_permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES

    def get(self, request, *args, **kwargs):
        self.check_method_permissions(self.retrieve_permission_classes, request)
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        self.check_method_permissions(self.update_permission_classes, request)
        return self.update(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        self.check_method_permissions(self.destroy_permission_classes, request)
        return self.destroy(request, args, kwargs)


class RetrieveDestroyAPIView(mixins.RetrieveModelMixin,
                             mixins.DestroyModelMixin,
                             MethodPermissionCheckAPIView):
    """
    Concrete view for retrieving or destroying a model instance.
    """
    retrieve_permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES
    destroy_permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES

    def get(self, request, *args, **kwargs):
        self.check_method_permissions(self.retrieve_permission_classes, request)
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.check_method_permissions(self.destroy_permission_classes, request)
        return self.destroy(request, args, kwargs)