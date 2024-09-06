from django.contrib import admin
from .models import Users

@admin.register(Users)
class User(admin.ModelAdmin):
    list_display = ['id','name', 'password']