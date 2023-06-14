from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'password', 'username',
                    'first_name', 'last_name', 'user_type']
