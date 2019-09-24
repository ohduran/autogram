from django.db import models


class ParaMixin(models.Model):

    para = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.para = self._password
        return super().save(*args, **kwargs)
