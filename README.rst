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

User Stamped Model Example:
---------------------------

  >>>  from django.contrib.auth.models import User
  >>>  from django.db import models
  >>>  from django.utils.translation import ugettext_lazy as _
  >>>  from edmu.models import UserStampedModel
  >>>
  >>>
  >>>  class ExampleModel(UserStampedModel):
  >>>      love_cake = models.BooleanField(_("loves cake"), default=True)
  >>>      love_dogs = models.BooleanField(_("loves dogs"), default=True)
  >>>
  >>>      class Meta:
  >>>          verbose_name = _("example")
  >>>          verbose_name_plural = _("examples")
  >>>
  >>>
  >>>  user = User.objects.get(pk=1)
  >>>
  >>>  temp = ExampleModel(
  >>>    love_cake=True,
  >>>    love_dogs=True
  >>>  )
  >>>
  >>>  # We must pass in the user that is saving the model. Both the ``created_by`` and ``updated_by`` fields will be
  >>>  # set because it is a new model.
  >>>  temp.save(user=user)
  >>>
  >>>  # Only the ``updated_by`` field will be set because it is not a new model.
  >>>  temp.love_cake = False
  >>>  temp.save(user=user)

The above example model will have an additional two fields. A ``created_by`` and a ``updated_by`` field that is
updated when the ``save`` method is called. The current ``user`` must be passed into the save method to let the model
know which user to set for the ``created_by`` and/or ``updated_by`` fields. Note that the ``created_by`` will only be
set for new models.