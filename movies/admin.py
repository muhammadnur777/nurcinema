from django.contrib import admin
from .models import MovieGenre, Movie

admin.site.register(Movie)
admin.site.register(MovieGenre)
