from functools import update_wrapper

from django.conf import settings
from django.contrib import admin
from django.contrib.admin.util import unquote
from django.contrib.admin.views.main import ChangeList
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.html import strip_spaces_between_tags as short
from django.utils.translation import ugettext_lazy as _


class UserStampedTabularInline(admin.TabularInline):
    """
    A django ``TabularInline`` class to handle saving ``Model``s that implement the ``UserStampedModel`` or
    ``UserTimeStampedModel`` classes.
    """
    readonly_fields = ("created_by", "updated_by")


class UserStampedStackedInline(admin.StackedInline):
    """
    A django ``TabularInline`` class to handle saving ``Model``s that implement the ``UserStampedModel`` or
    ``UserTimeStampedModel`` classes.
    """
    readonly_fields = ("created_by", "updated_by")


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
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        """
        """
        for obj in formset.save(commit=False):
            if not obj.pk:
                obj.created_by = request.user
            obj.updated_by = request.user
            obj.save()