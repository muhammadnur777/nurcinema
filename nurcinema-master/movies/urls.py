from django.urls import path
from .views import home, movie_detail, watch, blog


urlpatterns = [
    path('', home, name='home'),
    path('movie/<slug:slug>/', movie_detail, name='movie_detail'),
    path('watch/<slug:slug>/', watch, name='watch'),
    path('blog/', blog, name='our_blog')
    
    # path('Homepage/<slug:slug>/', home, name='home'),
]
