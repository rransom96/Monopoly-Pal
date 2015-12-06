from django.contrib.auth.models import User
from django.db import models


class Color(models.Model):
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.color


class Property(models.Model):
    color = models.ForeignKey(Color)
    price = models.IntegerField()
    probability = models.DecimalField(max_digits=2, decimal_places=1)
    rent = models.IntegerField()
    name = models.CharField(max_length=255)
    owner = models.ManyToManyField(User, through='Owned')

    def value(self):
        value = self.price/(self.probability*self.rent)
        user = User.objects.get(pk=1)
        for square in user.owned_set.all():
            if self.color == 9:
                value -= self.price/(2*square.property.probability*self.rent)
            elif self.color == square.property.color:
                value -= self.price/(5*square.property.probability*self.rent)
        return value

    def __str__(self):
        return self.name


class Owned(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    property = models.ForeignKey(Property, blank=True, null=True)

    def __str__(self):
        return "{} owns {}".format(self.user, self.property)

