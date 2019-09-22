from django.db import models

from ..commons.models import HasUser


class PictureQuerySet(models.QuerySet):
    pass


class Picture(HasUser, models.Model):
    objects = PictureQuerySet.as_manager()

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    owner = models.ForeignKey('owners.Owner', null=True, blank=True, on_delete=models.SET_NULL)

    name = models.TextField()
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
