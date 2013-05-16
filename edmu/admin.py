from django.contrib import admin


class UserStampedAdmin(admin.ModelAdmin):
    """
    A django ``ModelAdmin`` class to handle saving ``Model``s that implement the ``UserStampedModel`` or
    ``UserTimeStampedModel`` classes.
    """
    def save_model(self, request, obj, form, change):
        """
        """
        obj.save(user=request.user)