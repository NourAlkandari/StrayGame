from django.shortcuts import render
from .models import Pet, PetState, Food, Entertainment
from .serializers import PetDetailSerializer, PetStateSerializer, UserCreateSerializer
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

counter = 1
double_counter = counter * 2

# leave real time counter in frontend only (so we don't have to use websockets). Check time in frontend and then send a state change to backend. Can also have the timer pause and then restart with each function

####################### USER #######################

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

####################### PET #######################
# Details of the pet (static-ish)
class PetDetailView(RetrieveUpdateAPIView):
    serializer_class = PetDetailSerializer
    # only one pet, therefore only one object, so no need for object_id

    def get_object(self):
        # pet_obj, created = Pet.objects.get_or_create(user = request.user)
        # return pet_obj
        obj = Pet.objects.get(user=self.request.user) #do get or create
        return obj

# Details of the pet state (dynamic-ish)
class PetStateDetailView(RetrieveAPIView):
    serializer_class = PetStateSerializer
    
    def get_object(self):
        obj = PetState.objects.get(user=self.request.user)
        return obj

# create seperate url i.e. api
class NamePet(APIView):
    serializer_class = PetDetailSerializer

    def post(self,request):
        name = request.data.get("name")
        pet = Pet.objects.get(user=request.user)
        pet.name = name #changing the model field (specific to the user i.e. above) to the user generated name
        pet.save() #saving the pet object
        return Response(PetDetailSerializer(pet).data)


##################### ACTIONS #####################
# Functions i.e. The pet interactions that will alter the state of the pet. Must create a url for each action (interaction)
class FeedPet(APIView):
    serializer_class = PetStateSerializer

    def post(self, request):
        food = request.data.get("food") #"food" is the key from frontend. Setup an array in the frontend. Only type of variable that can be passed to backend is a dictionary (JSON) 
        pet = Pet.objects.get(user=request.user) #request.user only
        state = pet.state
# check the need level to cap it. Also add this validation in the front-end (user can't continue to feed pet if hunger is maxed out)
# get the food option from the front end and check if it matches one of the food options (string). No need for a model for Food (would not work anyway)
        if (state.hunger < 5) and (state.hunger >= 0):
            if food == "Dog Food":
                state.hunger= max(0, state.hunger + double_counter) # need to decide what kind of metric to follow (e.g. if "hunger" is high then pet is full or is the pet hungry?)
            if food == "Chocolate":
                state.hunger= max(0, state.hunger - double_counter) # add effect on mood later on
            if food == "Today's Lunch":
                state.hunger= max(0, state.hunger + counter)
        # OR below? Do I need the above if the serializer_class is already defined?
        # self.hunger = max(0, self.hunger - self.counter) #so you don't see negative hunger, duh!
        state.save()
        return Response(PetStateSerializer(pet.state).data) # self.hunger or state??

class EntertainPet(APIView):
    serializer_class = PetStateSerializer

    def post(self, request):
        entertainment = request.data.get("entertainment")
        pet = Pet.objects.get(user=request.user)
        state = pet.state
        if (state.fun < 5) and (state.fun >= 0):
            if entertainment == "Walk Pet":
                state.fun= max(0, state.fun + double_counter) 
            elif entertainment == "Ignore":
                state.fun= max(0, state.fun - double_counter) 
            elif entertainment == "Go to Petstore":
                state.fun= max(0, state.fun + counter)
        state.save()
        return Response(PetStateSerializer(pet.state).data)

    # def post(self, request):
    #     entertainment_options = request.data
    #     pet = Pet.objects.get(user=request.user)
    #     states = pet.states
    #     if Entertainment.options == Entertainment.Walk_Pet:
    #         states.hunger= max(0, states.hunger + double_counter) 
    #     elif Entertainment.options == Entertainment.Ignore:
    #         states.hunger= max(0, states.hunger - double_counter) 
    #     elif Entertainment.options == Entertainment.Go_to_Petstore:
    #         states.hunger= max(0, states.hunger + counter)
    #     states.save()
    #     return Response(PetStateSerializer(pet.states).data)

###############################################

# def mood(self):
#         if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
#             return "happy"
#         elif self.hunger > self.hunger_threshold:
#             return "hungry"
#         else:
#             return "bored"
