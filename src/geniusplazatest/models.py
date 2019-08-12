from django.db import models

# Create your models here.

class User(models.Model):
	username		= models.CharField(max_length=120, unique=True)
	email			= models.EmailField(unique=True)
	first_nmame		= models.CharField(max_length=120)
	last_name		= models.CharField(max_length=120)
	password		= models.CharField(max_length=120)

	def __str__(self):
		return str(self.username)



class Step(models.Model):
	step_text		= models.TextField(default = "unknown steps")	# also null = False (default value)
	recipe 			= models.ForeignKey('Recipe', on_delete=models.CASCADE, null=True)

class Ingredient(models.Model):
	text 			= models.TextField(default = "unknown ingredient")
	recipe 			= models.ForeignKey('Recipe', on_delete=models.CASCADE, null=True)


class Recipe(models.Model):
	name 			= models.TextField()
	user 			= models.OneToOneField(User, on_delete=models.CASCADE, related_name = "owner",)
	
	def __str__(self):
		return str(self.name)
