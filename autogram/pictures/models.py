from os.path import join

from django.db import models

from ..commons.models import HasUser, RandomQuerySet, Usable, UsableQuerySet


class PictureQuerySet(RandomQuerySet, UsableQuerySet, models.QuerySet):

    pass


class Picture(HasUser, Usable, models.Model):
    objects = PictureQuerySet.as_manager()

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    owner = models.ForeignKey('owners.Owner', null=True, blank=True, on_delete=models.SET_NULL)

    name = models.TextField()
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    file = models.FileField(upload_to='pictures/')

    @property
    def path(self):
        return self.file.path

    def __str__(self):
        return self.name
