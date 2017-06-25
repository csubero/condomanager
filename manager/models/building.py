from django.db import models


class Building(models.Model):
	name = models.CharField(max_length=250)
	address = models.TextField()
	rif = models.CharField(max_length=20)
	apartament_number = models.IntegerField()

	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name.title()
