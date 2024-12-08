from django.urls import path
from .views import login_view, logout_view, register, add_review

urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('add_review/', add_review, name='add_review')
]
