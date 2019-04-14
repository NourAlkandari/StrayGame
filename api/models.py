from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class PetDescription(models.Model):
	name = models.CharField(max_length=120)
	breed = models.CharField(max_length=120)
	weight = models.IntegerField()
	age = models.IntegerField()

class PetState(models.Model):
	fun = models.IntegerField(default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)])
	social = models.IntegerField(default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)])
	hunger = models.IntegerField(default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)])
	sleep = models.IntegerField(default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)])
	bladder = models.IntegerField(default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)])


# User is the account (how to connect to pet??)
# Need to connect pet states to pet

# class Items(models.Model):
# 	food = 
# 	toys = 
# 	health_kit = 
# 	bed = 


