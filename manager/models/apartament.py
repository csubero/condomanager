from django.db import models


class Apartament(models.Model):
	nomenclature = models.CharField(max_length=10)
	aliquot = models.DecimalField(max_digits=8, decimal_places=2)
	size = models.DecimalField(max_digits=8, decimal_places=2)

	building = models.ForeignKey('manager.Building', related_name='apartaments')

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nomenclature.upper()
