# from django.db.models import Model, ForeignKey, \
#     TextField, CASCADE, DateTimeField
# from django.contrib.auth.models import AbstractUser
# from django
# from movies.models import Movie


# class User(AbstractUser):
#     pass


# class UserReview(Model):
#     user = ForeignKey(User, on_delete=CASCADE)
#     movie = ForeignKey(Movie, on_delete=CASCADE)    
#     comment = TextField()
#     posted = DateTimeField(auto_created=True)

from django.db.models import Model, ForeignKey, \
    TextField, CASCADE, DateTimeField
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from movies.models import Movie



class User(AbstractUser):
    pass


# class Ban_User(Model):
#     user = ForeignKey(User)


class UserReview(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    movie = ForeignKey(Movie, on_delete=CASCADE)
    comment = TextField()
    posted = DateTimeField(auto_now_add=True)

    def time_posted(self):
      
        delta = now() - self.posted

        if delta.days > 0:
            if delta.days == 1:
                return "1 day ago"
            return f"{delta.days} days ago"
        elif delta.seconds // 3600 > 0:
            hours = delta.seconds // 3600
            if hours == 1:
                return "1 hour ago"
            return f"{hours} hours ago"
        elif delta.seconds // 60 > 0:
            minutes = delta.seconds // 60
            if minutes == 1:
                return "1 minute ago"
            return f"{minutes} minutes ago"
        return "Just now"

