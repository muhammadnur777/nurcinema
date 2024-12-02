from django.shortcuts import render
from .models import Movie, MovieGenre, \
    MovieStatusChoices, MovieTypeChoices, Genre

from django.core.cache import cache


def home(request):
    banners = Movie.objects.filter(type=MovieTypeChoices.BANNER)[:3]
    regular = Movie.objects.filter(type=MovieTypeChoices.REGULAR)
    top_views = Movie.objects.all().order_by('-views')[:5]


    context = {
        'banners': banners,
        'regular': regular,
        'top_views': top_views
        # 'movie_detail_slug': movie_detail_slug
    }
    print(f"{banners=}")

    return render(request, 'index.html', context=context)


def movie_detail(request, slug):
    movies = Movie.objects.get(slug=slug)

    context = {
        'movie': movies
    }


    return render(request, 'movie-details.html', context=context)


def watch(request, slug):
    movie = Movie.objects.get(slug=slug)
    cache_key = f"movie_{slug}"
    key = cache.get(cache_key, None)
    if key is None:

        movie.views += 1
        views = movie.views
        movie.save()
        cache.set(cache_key, views, timeout=2)


    

    context = {
        'movie': movie
    }    

    return render(request, 'movie-watching.html', context=context)


def blog(request):
    return render(request, 'blog.html')

def categories(request):
    return render(request, 'categories.html')