import random
from faker import Faker
from django.core.management.base import BaseCommand
from movies.models import Movie, Genre, MovieGenre, QualityChoices, MovieStatusChoices, MovieTypeChoices

fake = Faker()


file_names = [
    'movie_images/1.jpg', 'movie_images/2.jpg', 'movie_images/3.jpg'
]

video_files = [

    'movies/Mufasa.mp4', 'movies/Red_one.mp4'
]

class Command(BaseCommand):
    help = "Populate the database with random movies and genres"

    def handle(self, *args, **kwargs):
        self.create_genres()
        self.create_movies()
        self.stdout.write(self.style.SUCCESS("Successfully populated the database!"))

    def create_genres(self):
        genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Documentary']
        for genre_name in genres:
            Genre.objects.get_or_create(name=genre_name)

    def create_movies(self):
        genres = list(Genre.objects.all())
        for _ in range(25):  # Adjust the number of movies as needed
            movie = Movie.objects.create(
                title=fake.sentence(nb_words=random.randrange(3, 7)),
                description=fake.paragraph(nb_sentences=random.randrange(5, 10)),
                duration=random.randint(80, 180),
                movie_type=fake.word(ext_word_list=["Action", "Romance", "Thriller", "Animation"]),
                studios=fake.company(),
                release_date=fake.date_between(start_date="-10y", end_date="today"),
                rating=round(random.uniform(1, 10), 1),
                views=random.randint(1000, 100000),
                is_active=random.choice([True, False]),
                quality=random.choice([choice[0] for choice in QualityChoices.choices]),
                scores=round(random.uniform(0, 10), 1),
                status=random.choice([choice[0] for choice in MovieStatusChoices.choices]),
                type=random.choice([choice[0] for choice in MovieTypeChoices.choices]),
                slug=None,  # Automatically generated in `save` method
                image=random.choice(file_names),
                video=random.choice(video_files),
                thumb=fake.file_name(category="image"),
            )
            movie.save()

            # Assign random genres to the movie
            assigned_genres = random.sample(genres, random.randint(1, 3))
            for genre in assigned_genres:
                MovieGenre.objects.create(movie=movie, genre=genre)
