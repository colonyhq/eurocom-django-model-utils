=========
Changelog
=========

0.2.2 (2013-08-02)
==================

- Fixed an issue with multiple inheritance errors.

0.2.1 (2013-08-02)
==================

- The parameters being sent into the UUID field are incorrect.

0.2.0 (2013-08-02)
==================

- Added a BaseModel that has a primary key as a UUID field. This BaseModel is also inherited by all previous models.

0.1.2 (2013-07-30)
==================

- Changed the edmu.models to get the User Model from settings.AUTH_USER_MODEL instead.

0.1.1 (2013-07-18)
==================

- Updated the User import on models to be Django 1.5+ compatible.

0.1 (2013-05-16)
================

- Has three abstract model classes for time stamped, user stamped and time + user stamped models.
- Added an admin class to handle UserStampedModel and UserTimeStampedModel classes.
- Added an admin inline classes to handle UserStampedModel and UserTimeStampedModel classes.