from django.db import models

from manager.models.person import Person


class Owner(Person):
	apartaments = models.ManyToManyField('manager.Apartament', related_name='owner')
