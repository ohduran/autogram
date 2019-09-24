from random import sample

from django.db import models


class NaturalKeyableQuerySet(models.QuerySet):

    def get_by_natural_key(self, natural_key):
        return self.get(**{self.model._natural_key: natural_key})


class RandomQuerySet(models.QuerySet):

    def random(self, _quantity=1):
        values_list = list(self.values_list('id', flat=True))
        if not values_list:
            return self
        random_selection = sample(values_list, _quantity)
        return self.filter(id__in=random_selection)

    def get_object_or_random(self, **kwargs):
        if not kwargs:
            return self.random().first()
        return self.get(**kwargs)


class UsableQuerySet(models.QuerySet):

    def least_used(self):
        """Take those with the least amount of times_used."""
        try:
            min_times_used = min(self.values_list('times_used', flat=True))
            return self.filter(times_used=min_times_used)
        except ValueError:
            return self
