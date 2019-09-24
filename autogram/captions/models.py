from django.db import models

from ..commons.models import HasUser, NaturalKeyable, NaturalKeyableQuerySet, RandomQuerySet, Usable, UsableQuerySet


class CaptionQuerySet(NaturalKeyableQuerySet, RandomQuerySet, UsableQuerySet, models.QuerySet):

    pass


class Caption(HasUser, NaturalKeyable, Usable, models.Model):

    text = models.TextField(unique=True)
    objects = CaptionQuerySet.as_manager()

    _natural_key = 'text'
