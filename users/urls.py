from django.urls import path
from .views import login_view, logout_view, register

urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login')
]
