from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Pet, PetState

class PetDetailSerializer(serializers.ModelSerializer):
	states = PetStateSerializer() #if using all, use the same field name!!!

    class Meta:
        model = Pet
        fields = '__all__'

class PetStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetState
        fields = '__all__'