import random
from faker import Faker
from django.core.management.base import BaseCommand
from movies.models import Movie, Genre, MovieGenre, QualityChoices, MovieStatusChoices, MovieTypeChoices

fake = Faker()


file_names = [
    'movie_images/shrek5jpg', 'movie_images/БИТВА ПАП.jpg',
    'movie_images/В БАНЮ.jpg', 'movie_images/веном 3.jpg', 'movie_images/Гладиатор 2.jpg', 'movie_images/Крик.jpg',
    'movie_images/Лунтик.jpg', 'movie_images/Маша и Медведь.jpg', 'movie_images/Моана 2.jpg', 'movie_images/Назад к динозаврам.jpg',
    'movie_images/Операция Панда.jpg', 'movie_images/пес.jpg', 'movie_images/Приключения Паддингтона 3.jpg', 
    'movie_images/Смешарики снимают кино.jpg', 'movie_images/СОНИК 3 В КИНО.jpg', 'movie_images/Субстанция.jpg',
    'movie_images/Супер Крылья.jpg', 'movie_images/Три кота. Зимние каникулы.jpg', 'movie_images/Чебурашка.jpg',
    'movie_images/Черная Пантера 2.jpg'
]

movie_title = [
    'shrek5', 'БИТВА ПАП',
    'в баню2', 'веном 3', 'гладиатор 2', 'крик',
    'Лунтик', 'Маша и Медведь', 'Моана 2', 'Назад к динозаврам',
    'Операция Панда', 'пес.jpg', 'Приключения Паддингтона 3', 
    'Смешарики снимают кино', 'СОНИК 3 В КИНО', 'Субстанция',
    'Супер Крылья', 'Три кота. Зимние каникулы', 'Чебурашка',
    'Черная Пантера 2'
]

video_files = [

    'movies/shrek5.mp4', 'movies/БИТВА ПАП.mp4',
    'movies/В БАНЮ.mp4', 'movies/Веном 3.mp4', 'movies/Гладиатор 2.mp4', 'movies/Крик.mp4', 
    'movies/Лунтик.mp4', 'movies/Маша и Медведь.mp4', 'movies/Моана 2.mp4', 'movies/Назад к динозаврам.mp4',
    'movies/Операция Панда.mp4', 'movies/пес.mp4', 'movies/Приключения Паддингтона 3.mp4',
    'movies/Смешарики снимают кино .mp4', 'movies/СОНИК 3 В КИНО.mp4', 'movies/Субстанция .mp4',
    'movies/Супер Крылья.mp4', 'movies/Три кота. Зимние каникулы .mp4', 'movies/Чебурашка.mp4',
    'movies/Черная Пантера 2.mp4'
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
        for i in range(20):  # Adjust the number of movies as needed
            print(f"{i=}")
            print(f"{movie_title[i]=}")
            movie = Movie.objects.create(
                title=movie_title[i],
                description=fake.paragraph(nb_sentences=random.randrange(5, 10)),
                duration=random.randint(80, 180),
                movie_type=fake.word(ext_word_list=["Action", "Romance", "Thriller", "Animation"]),
                studios=fake.company(),
                release_date=fake.date_between(start_date="-10y", end_date="today"),
                rating=round(random.uniform(4, 100), 1),
                views=random.randint(100, 10000),
               
                quality=random.choice([choice[0] for choice in QualityChoices.choices]),
                scores=round(random.uniform(4, 10), 1),
                status=random.choice([choice[0] for choice in MovieStatusChoices.choices]),
                type=random.choice([choice[0] for choice in MovieTypeChoices.choices]),
              
                image=file_names[i],
                video=video_files[i],
                thumb=video_files[i],
            )
            movie.save()

            # Assign random genres to the movie
            assigned_genres = random.sample(genres, random.randint(1, 3))
            for genre in assigned_genres:
                MovieGenre.objects.create(movie=movie, genre=genre)
