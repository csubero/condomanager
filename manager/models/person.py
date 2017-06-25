from django.db import models


class Person(models.Model):
	identification_card = models.CharField(max_length=12)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{0} {1}'.format(self.first_name, self.last_name)

	class Meta:
		abstract = True
