from rest_framework_mongoengine import generics
from edmu.api.mixins import MethodPermissionCheckAPIView, DestroyAPIView


class MongoListAPIView(generics.ListAPIView, MethodPermissionCheckAPIView):
    """
    View for listing objects. It also implements the MethodPermissionCheckAPIView to allow for finer grained method
    permission checking.
    """


class MongoRetrieveAPIView(generics.RetrieveAPIView, MethodPermissionCheckAPIView):
    """
    View for getting an object. It also implements the MethodPermissionCheckAPIView to allow for finer grained method
    permission checking.
    """


class MongoUpdateAPIView(generics.UpdateAPIView, MethodPermissionCheckAPIView):
    """
    View for updating an object. It also implements the MethodPermissionCheckAPIView to allow for finer grained method
    permission checking.
    """


class MongoDestroyAPIView(DestroyAPIView, MethodPermissionCheckAPIView):
    """
    View for deleting an object. It also implements the MethodPermissionCheckAPIView to allow for finer grained method
    permission checking.
    """


class MongoListCreateAPIView(generics.ListCreateAPIView, MethodPermissionCheckAPIView):
    """
    View for listing objects or creating an object. It also implements the MethodPermissionCheckAPIView to allow for
    finer grained method permission checking.
    """


class MongoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView, MethodPermissionCheckAPIView):
    """
    View for getting, updating or deleting an object. It also implements the MethodPermissionCheckAPIView to allow for
    finer grained method permission checking.
    """


class MongoRetrieveUpdateAPIView(generics.RetrieveAPIView, generics.UpdateAPIView, MethodPermissionCheckAPIView):
    """
    View for getting or updating an object. It also implements the MethodPermissionCheckAPIView to allow for finer
    grained method permission checking.
    """


class MongoRetrieveDestroyAPIView(generics.RetrieveAPIView, DestroyAPIView, MethodPermissionCheckAPIView):
    """
    View for getting or deleting an object. It also implements the MethodPermissionCheckAPIView to allow for finer
    grained method permission checking.
    """


class MongoUpdateDestroyAPIView(generics.UpdateAPIView, DestroyAPIView, MethodPermissionCheckAPIView):
    """
    View for updating or deleting an object. It also implements the MethodPermissionCheckAPIView to allow for finer
    grained method permission checking.
    """