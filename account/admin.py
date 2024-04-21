from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(UserAdmin):
    model = User
    # Customize list_display, fieldsets, etc. as needed
    list_display = ['mobile_number','email', 'first_name', 'last_name', 'is_active', 'is_staff']
    # Define ordering with fields from your custom user model
    ordering = ['email']


admin.site.register(User, UserAdmin)
