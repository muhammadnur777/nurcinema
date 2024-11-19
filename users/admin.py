from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import register
from .models import User

@register(User)
class CustomUserAdmin(UserAdmin):
    pass