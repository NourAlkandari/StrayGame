"""StrayGame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from .views import CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView, APIView

from api import views

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', views.UserCreateAPIView.as_view(), name='register'),

    # Pet Details and States
    path('pet/', views.PetDetailView.as_view(), name='pet-details'),
    # path('pet/states/', views.PetStateDetailView.as_view(), name='pet-states'), #Don't think another api is needed if the first one is connected to the states

    # Pet Interactions
    path('pet/name/', views.NamePet.as_view(), name='name-pet'),
    path('pet/feed/', views.FeedPet.as_view(), name='feed-pet'),
    path('pet/entertain/', views.EntertainPet.as_view(), name='entertain-pet'),
    path('pet/sleep/', views.PutPetToBed.as_view(), name='sleep-pet'),

    path('pet/syringe/', views.MakePetHealthy.as_view(), name='make-pet-healthy'),






]
