from random import sample

from django.db import models


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
