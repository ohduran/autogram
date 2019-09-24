from django.db import models

from ..commons.models import HasUser


class OwnerQuerySet(models.QuerySet):

    def unflagged(self):
        return self.filter(flagged=False)

    def flag(self):
        return self.update(flagged=True)


class Owner(HasUser, models.Model):

    username = models.CharField(unique=True, max_length=30)
    instagram_id = models.CharField(max_length=30)
    flagged = models.BooleanField(default=False)

    def flag(self):
        return self.update(flagged=True)

    def __str__(self):
        return f"@{self.username}"
