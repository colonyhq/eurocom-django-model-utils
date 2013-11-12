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


class OrderedModelAdmin(admin.ModelAdmin):
    def get_urls(self):
        from django.conf.urls import patterns, url

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)
        info = self.model._meta.app_label, self.model._meta.module_name
        return patterns('',
            url(r'^(.+)/move-(up)/$',
                wrap(self.move_view),
                name='%s_%s_move_up' % info),
            url(r'^(.+)/move-(down)/$',
                wrap(self.move_view),
                name='%s_%s_move_down' % info),
        ) + super(OrderedModelAdmin, self).get_urls()

    def _get_changelist(self, request):
        list_display = self.get_list_display(request)
        list_display_links = self.get_list_display_links(request, list_display)

        cl = ChangeList(request, self.model, list_display,
            list_display_links, self.list_filter, self.date_hierarchy,
            self.search_fields, self.list_select_related,
            self.list_per_page, self.list_max_show_all, self.list_editable,
            self)

        return cl

    request_query_string = ''

    def changelist_view(self, request, extra_context=None):
        cl = self._get_changelist(request)
        self.request_query_string = cl.get_query_string()
        return super(OrderedModelAdmin, self).changelist_view(request, extra_context)

    def move_view(self, request, object_id, direction):
        cl = self._get_changelist(request)
        qs = cl.get_query_set(request)

        obj = get_object_or_404(self.model, pk=unquote(object_id))
        obj.move(direction, qs)

        return HttpResponseRedirect('../../%s' % self.request_query_string)

    def move_up_down_links(self, obj):
        link_html = short("""
            <a href="../../%(app_label)s/%(module_name)s/%(object_id)s/move-up/%(query_string)s">
                <img src="%(STATIC_URL)sordered_model/arrow-up.gif" alt="Move up" />
            </a>
            <a href="../../%(app_label)s/%(module_name)s/%(object_id)s/move-down/%(query_string)s">
                <img src="%(STATIC_URL)sordered_model/arrow-down.gif" alt="Move down" />
            </a>""")

        return link_html % {
            'app_label': self.model._meta.app_label,
            'module_name': self.model._meta.module_name,
            'object_id': obj.pk,
            'STATIC_URL': settings.STATIC_URL,
            'query_string': self.request_query_string
        }
    move_up_down_links.allow_tags = True
    move_up_down_links.short_description = _(u'Move')