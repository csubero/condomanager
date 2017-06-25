from django.db import models


class Phone(models.Model):
	number = models.CharField(max_length=50)

	owner = models.ForeignKey('manager.Owner', related_name='phones')
