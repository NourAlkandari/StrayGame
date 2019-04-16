from django.shortcuts import render
from .models import PetDescription, PetState, Food
from .serializers import PetDetailSerializer, PetStateSerializer,
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

counter = 1
bonus_counter = counter * 2

# Details of the pet (static-ish)
class PetDetailView(RetrieveUpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

# Details of the pet state (dynamic-ish)
class PetStateDetailView(RetrieveAPIView):
    queryset = PetState.objects.all()
    serializer_class = PetStateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

# Functions i.e. The pet interactions that will alter the state of the pet. Must create a url for each action (interaction)
class FeedPet(APIView):
    serializer_class = PetStateSerializer

    def post(self, request):
    	food_options = request.data
    	pet = Pet.objects.get(user=request.user)
    	states = pet.states
    	if Foods.food_choice == Foods.Dog_Food:
    		states.hunger= max(0, states.hunger - decrement)
    	elif Foods.food_choice == Foods.Chocolate:
    		states.hunger= max(0, states.hunger - decrement)
    	elif Foods.food_choice == Foods.Todays_Lunch:
    		states.hunger= max(0, states.hunger - decrement)
    	# OR below? Do I need the above if the serializer_class is already defined?
    	# self.hunger = max(0, self.hunger - self.decrement) #so you don't see negative hunger, duh!
    	states.save()
    	return Response(PetStateSerializer(pet.states).data) # self.hunger or state??

###############################################

# def mood(self):
#         if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
#             return "happy"
#         elif self.hunger > self.hunger_threshold:
#             return "hungry"
#         else:
#             return "bored"
