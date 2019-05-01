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
    # mood = serializers.SerializerMethodField()
    healthy = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = '__all__'

    def get_age(self, obj):
        user = obj.user
        now = datetime.datetime.now(datetime.timezone.utc)
        new_age = (now - user.date_joined).days
        return new_age

    # def get_mood(self,obj):
    #     state = Pet.objects.get(user=request.user).state
    #     if (state.fun >= 80 and state.fun <= 100) and (state.hunger >= 80 and state.hunger <= 100) and (state.social >= 80 and state.social <= 100) and (state.sleep >= 80 and state.sleep <= 100) and (state.bladder >= 80 and state.bladder <= 100):
    #         return "Happy"
    #     elif (state.fun >= 35 and state.fun < 80) and (state.hunger >= 35 and state.hunger < 80) and (state.social >= 35 and state.social < 80) and (state.sleep >= 35 and state.sleep < 80) and (state.bladder >= 35 and state.bladder < 80):
    #         return "Neutral"
    #     else:
    #         return "Sad"

    def get_healthy(self, obj):
        state = Pet.objects.get(user=request.user).state
        if (((state.fun+state.social+state.hunger+state.sleep+state.bladder)/5) <= 25):
            return False
        else:
            return True


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

