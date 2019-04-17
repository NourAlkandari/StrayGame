from django.contrib import admin
from .models import Pet, PetState
# Register your models here.
admin.site.register(Pet)
admin.site.register(PetState)