try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()

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
    An abstract base class model that provides self-updating ``created_by`` and ``updated_by`` fields. To be able to
    save the user's information in the the ``created_by`` and ``updated_by`` fields, the ``user`` argument must be
    set when instantiating the class.

    To user ``UserStampedModel``, the user model needs to be passed in the ``save`` method via ``user``.
    """
    created_by = models.ForeignKey(User, verbose_name=_("created by"),
                                   related_name="%(app_label)s_%(class)s_created_by")
    updated_by = models.ForeignKey(User, verbose_name=_("updated by"),
                                   related_name="%(app_label)s_%(class)s_updated_by")

    class Meta:
        abstract = True

    def save(self, user, force_insert=False, force_update=False, using=None):
        """
        We need to check that the user was actually passed in. We only set the ``created_by`` attribute if this is a
        new object by checking the ``pk``.
        """
        # We only set the ``created_by`` field if the model is new (i.e. has not pk).
        if not self.pk:
            self.created_by = user
        self.updated_by = user

        super(UserStampedModel, self).save(
            force_insert=force_insert,
            force_update=force_update,
            using=using
        )


class UserTimeStampedModel(TimeStampedModel, UserStampedModel):
    """
    An abstract base class model that provides self-updating ``date_created``, ``date_updated``, ``created_by`` and
    ``updated_by`` fields. To be able to save the user's information in the the ``created_by`` and ``updated_by``
    fields, the ``user`` argument must be set when instantiating the class.
    """
    class Meta:
        abstract = True