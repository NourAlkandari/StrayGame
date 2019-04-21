from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Pet, PetState, Food, Entertainment

class PetStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetState
        fields = '__all__'

class PetDetailSerializer(serializers.ModelSerializer):
    state = PetStateSerializer() #if using all, use the same field name!!!

    class Meta:
        model = Pet
        fields = '__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        Pet.objects.create()
        new_user.save()
        return validated_data