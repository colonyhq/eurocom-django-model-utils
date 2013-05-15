from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating ``date_created`` and ``date_updated`` fields.
    """
    date_created = models.DateTimeField(_("date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("date updated"), auto_now=True)

    class Meta:
        abstract = True


class UserStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating ``created_by`` and ``updated_by`` fields.
    """
    created_by = models.ForeignKey(User, verbose_name=_("created by"))
    updated_by = models.ForeignKey(User, verbose_name=_("updated by"))

    class Meta:
        abstract = True


class UserTimeStampedModel(TimeStampedModel, UserStampedModel):
    """
    An abstract base class model that provides self-updating ``date_created``, ``date_updated``, ``created_by`` and
    ``updated_by`` fields.
    """
    class Meta:
        abstract = True