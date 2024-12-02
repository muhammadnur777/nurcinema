from django.db.models import Model, ForeignKey, \
    TextField, CASCADE
from django.contrib.auth.models import AbstractUser
from movies.models import Movie


class User(AbstractUser):
    pass


class UserReview(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    movie = ForeignKey(Movie, on_delete=CASCADE)
    comment = TextField()
