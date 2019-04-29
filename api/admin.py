from django.contrib import admin
from .models import Pet, PetState

class PetStateInline(admin.TabularInline):
    model = Pet


@admin.register(PetState)
class PetAdmin(admin.ModelAdmin):
    inlines = [PetStateInline]


# Register your models here.
admin.site.register(Pet)
# admin.site.register(PetState)