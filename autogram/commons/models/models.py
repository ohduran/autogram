from django.db import models


class HasUser(models.Model):

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        abstract = True
