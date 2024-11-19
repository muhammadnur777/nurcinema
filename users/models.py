from django.db.models import Model, ForeignKey, \
    TextField, SET_NULL, CASCADE
from django.contrib.auth.models import AbstractUser
from movies.models import Movie


class User(AbstractUser):
    pass


class UserReview(Model):
    user = ForeignKey(User, on_delete=SET_NULL)
    movie = ForeignKey(Movie, on_delete=CASCADE)
    comment = TextField()
