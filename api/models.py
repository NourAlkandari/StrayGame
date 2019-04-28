from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from random import randrange
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Pet Needs (dynamic details)
class PetState(models.Model):
    fun = models.IntegerField(default=20,
        validators=[MaxValueValidator(100), MinValueValidator(1)])
    social = models.IntegerField(default=20 ,
        validators=[MaxValueValidator(100), MinValueValidator(1)])
    hunger = models.IntegerField(default=20,
        validators=[MaxValueValidator(100), MinValueValidator(1)])
    sleep = models.IntegerField(default=20,
        validators=[MaxValueValidator(100), MinValueValidator(1)])
    bladder = models.IntegerField(default=20,
        validators=[MaxValueValidator(100), MinValueValidator(1)])

    def __str__(self):
        return "Fun: " + str(self.fun) + " Hunger: " + str(self.hunger)

###############################################
# Pet "Static" Details
class Pet(models.Model):
    name = models.CharField(max_length=120, null=True)
    breed = models.CharField(max_length=120, default="Mix-breed")
    weight = models.DecimalField(default=4, decimal_places=2, max_digits=4) #or float field, add decimal points later!!
    age = models.IntegerField(default=3)
    state = models.OneToOneField(PetState, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        # if self.name:
        #     return self.name + str(self.state.id)
      return self.name 

    def needs(self):
        self.state.fun = max(0,self.state.fun - 20)
        self.state.social = max(0, self.state.social - 20)
        self.state.hunger = max(0, self.state.hunger - 20)
        self.state.sleep = max(0, self.state.sleep - 20)
        self.state.bladder = max(0, self.state.bladder - 20)
        self.state.save()

# decorater, takes an instance of the User model and creates a pet. First, you have to create a pet state and then a pet for the user (since pet state is part of Pet model). Post_save means "do this once a User is save i.e. created"
# commad + ctrl + arrow up or down
@receiver(post_save, sender=User)
def users_pet(instance, created, *args, **kwargs):
    if created:
        state = PetState.objects.create() # shifted this upwards, jic. Cause many petState objects were created on the admin site 
        Pet.objects.create(user=instance, state=state) #only non-defaults

# Initializes pet states [is this even necessary for an API?]
    # def __init__(self):
    #     self.name = name
    #     self.fun = fun
    #     self.social = social
    #     self.hunger = hunger
    #     self.sleep = sleep
    #     self.bladder = bladder

 

###############################################
# Make a model for all "items" with options in the game
class Food(models.Model):
    Dog_Food = "Dog Food"
    Chocolate = "Chocolate"
    Todays_Lunch = "Today's Lunch"

    FOOD_OPTIONS = (
        (Dog_Food,Dog_Food),
        (Chocolate,Chocolate),
        (Todays_Lunch,Todays_Lunch)
        )

    options = models.CharField(choices=FOOD_OPTIONS, max_length=120)

class Entertainment(models.Model):
    Walk_Pet = "Take Pet for a Walk"
    Ignore = "Ignore"
    Go_to_Petstore = "Go to Petstore"

    Entertainment_Options = (
        (Walk_Pet,Walk_Pet),
        (Ignore,Ignore),
        (Go_to_Petstore,Go_to_Petstore)
        )

    options = models.CharField(choices=Entertainment_Options, max_length=120)

###############################################
############ Example of Tamagotchi ############

# class Pet():
#     boredom_decrement = 4
#     hunger_decrement = 6
#     boredom_threshold = 5
#     hunger_threshold = 10
#     sounds = ['Mrrp']

#     def __init__(self, name = "Kitty"):
#         self.name = name
#         self.hunger = randrange(self.hunger_threshold)
#         self.boredom = randrange(self.boredom_threshold)
#         self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

#     def clock_tick(self):
#         self.boredom += 1
#         self.hunger += 1

#     def mood(self):
#         if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
#             return "happy"
#         elif self.hunger > self.hunger_threshold:
#             return "hungry"
#         else:
#             return "bored"

#     def __str__(self):
#         state = "     I'm " + self.name + ". "
#         state += " I feel " + self.mood() + ". "
#         # state += "Hunger {} Boredom {} Words {}".format(self.hunger, self.boredom, self.sounds)
#         return state

#     def hi(self):
#         print self.sounds[randrange(len(self.sounds))]
#         self.reduce_boredom()

#     def teach(self, word):
#         self.sounds.append(word)
#         self.reduce_boredom()

#     def feed(self):
#         self.reduce_hunger()

#     def reduce_hunger(self):
#         self.hunger = max(0, self.hunger - self.hunger_decrement)

#     def reduce_boredom(self):
#         self.boredom = max(0, self.boredom - self.boredom_decrement)


###############################################
# User is the account (how to connect to pet??)
# Need to connect pet states to pet

# class Items(models.Model):
#   food = 
#   toys = 
#   health_kit = 
#   bed = 


