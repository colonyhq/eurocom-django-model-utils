from django.contrib import admin

from .models import UserStampedModel


class UserStampedAdmin(admin.ModelAdmin):
    """
    A django ``ModelAdmin`` class to handle saving ``Model``s that implement the ``UserStampedModel`` or
    ``UserTimeStampedModel`` classes.
    """
    readonly_fields = ("created_by", "updated_by")

    def save_model(self, request, obj, form, change):
        """
        We need to pass the user to the save method as it is what the underlying model expects.
        """
        obj.save(user=request.user)

    def save_formset(self, request, form, formset, change):
        """
        """
        for obj in formset.save(commit=False):
            if issubclass(obj, UserStampedModel):
                obj.save(user=request.user)
            else:
                obj.save()