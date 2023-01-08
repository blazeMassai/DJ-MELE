from django.contrib import admin
from .models import Profiles


# Register your models here.
@admin.register(Profiles)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']
