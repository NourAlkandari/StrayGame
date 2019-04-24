from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Pet, PetState, Food, Entertainment
import datetime
from rest_framework_jwt.settings import api_settings

# from django.utils.timezone import now


class PetStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetState
        fields = '__all__'

class PetDetailSerializer(serializers.ModelSerializer):
    state = PetStateSerializer() #if using all, use the same field name!!!
    age = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = '__all__'

    def get_age(self, obj):
        user = obj.user
        now = datetime.datetime.now(datetime.timezone.utc)
        new_age = (now - user.date_joined).days
        print(new_age)
        return new_age

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email','token']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(new_user)
        token = jwt_encode_handler(payload)

        validated_data["token"] = token
        return validated_data

