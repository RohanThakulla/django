from django.db import models

# Create your models here.

class contact(models.model):
	name = models.CharField(max_length = 300)
	email = models.CharField(max_length = 300)
	subject = models.TextField()
	messages = models.TextField()

	def __str__(self):
		return f'{self.name} has sent you message '


class info(models.model):
	address = models.CharField(max_length = 300)
	local_address = models.ChaField(max_length = 300)
	phone = models.ChaField(max_length = 200)
	time = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)

	def __str__(self):
		return self.address

