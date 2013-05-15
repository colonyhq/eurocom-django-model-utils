==========================
EUROCOM Django Model Utils
==========================

EDMU is a collection of abstract classes to use with Django Models.

Time Stamped Model Example:
---------------------------

  >>>  from django.db import models
  >>>  from django.utils.translation import ugettext_lazy as _
  >>>  from edmu.models import TimeStampedModel
  >>>
  >>>
  >>>  class ExampleModel(TimeStampedModel):
  >>>      first_name = models.CharField(_("name"), max_length=30)
  >>>      last_name = models.CharField(_("name"), max_length=30)
  >>>
  >>>      class Meta:
  >>>          verbose_name = _("example")
  >>>          verbose_name_plural = _("examples")

The above example model will have an additional two fields. A ``date_created`` and a ``date_updated`` field that is
automatically updated when data is added and updated.