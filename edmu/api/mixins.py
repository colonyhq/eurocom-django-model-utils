from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.settings import api_settings


class UserStampedMixin(object):
    """
    """
    def create(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = self.get_serializer(data=request.DATA, files=request.FILES)

        if serializer.is_valid():
            self.pre_save(serializer.object)
            self.object = serializer.save(force_insert=True, user=request.user)
            self.post_save(self.object, created=True)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                            headers=headers)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        partial = kwargs.pop('partial', False)
        self.object = self.get_object_or_none()

        if self.object is None:
            created = True
            save_kwargs = {'force_insert': True}
            success_status_code = status.HTTP_201_CREATED
        else:
            created = False
            save_kwargs = {'force_update': True}
            success_status_code = status.HTTP_200_OK

        serializer = self.get_serializer(self.object, data=request.DATA,
                                         files=request.FILES, partial=partial)

        if serializer.is_valid():
            save_kwargs.update({'user': request.user})
            self.pre_save(serializer.object)
            self.object = serializer.save(**save_kwargs)
            self.post_save(self.object, created=created)
            return Response(serializer.data, status=success_status_code)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class ObjectPermissionCheckAPIView(GenericAPIView):
    """
    Mixin to add methods to handle the getting and checking of object permissons.
    """
    def check_object_permissions(self, permission_classes, request, obj):
        """
        Check if the request should be permitted for a given object.
        Raises an appropriate exception if the request is not permitted.
        """
        for permission in [p() for p in permission_classes]:
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


class RetrieveUpdateAPIView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            MethodPermissionCheckAPIView):
    """
    Concrete view for retrieving or updating a model instance.
    """
    retrieve_permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES
    update_permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES

    def get(self, request, *args, **kwargs):
        self.check_method_permissions(self.retrieve_permission_classes, request)
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        self.check_method_permissions(self.update_permission_classes, request)
        return self.update(request, args, kwargs)


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