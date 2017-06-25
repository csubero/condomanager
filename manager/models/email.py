from django.db import models


class Email(models.Model):
	email = models.CharField(max_length=254)

	owner = models.ForeignKey('manager.Owner', related_name='emails')
