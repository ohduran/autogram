from django.db import models


class HasUser(models.Model):

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class NaturalKeyable(models.Model):

    class Meta:
        abstract = True

    def natural_key(self):
        natural_key = getattr(self, self._natural_key)
        return (natural_key,)


class Usable(models.Model):

    times_used = models.IntegerField(default=0)

    class Meta:
        abstract = True
