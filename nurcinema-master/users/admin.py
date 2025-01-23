from django.contrib.auth.admin import UserAdmin 
from django.contrib.admin import register
from .models import User,UserReview
from django.contrib import admin


admin.site.register(UserReview)
