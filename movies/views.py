from django.shortcuts import render
from .models import Movie, MovieGenre, \
    MovieStatusChoices, MovieTypeChoices, Genre
from django.contrib.auth import get_user_model
from users.models import UserReview
from django.core.cache import cache
from django.db.models import Q

def home(request):
    banners = Movie.objects.filter(type=MovieTypeChoices.BANNER).order_by('id')[:3]
    regular = Movie.objects.filter(type=MovieTypeChoices.REGULAR)
    top_views = Movie.objects.all().order_by('-views')[:5]

    q = request.GET.get('q')

    if q:
        regular = regular.filter(title__icontains=q)

    context = {
        'banners': banners,
        'regular': regular,
        'top_views': top_views
        # 'movie_detail_slug': movie_detail_slug
    }
    print(f"{banners=}")

    return render(request, 'index.html', context=context)


def blog(request):
    
    return render(request, 'blog.html')

    

def movie_detail(request, slug):
    
    movies = Movie.objects.get(slug=slug)

       
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            movie = Movie.objects.get(slug=slug)
            comment = request.POST.get('comment')
            UserReview.objects.create(
                user=user, movie=movie, comment=comment
            )
    reviews = UserReview.objects.filter(movie=movie).order_by('-id')
    you_might_like = Movie.objects.filter(type=movies.type)[:4]
   
    context = {
        'movie': movies,
        'reviews': reviews,
        'you_might_like': you_might_like
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



    if request.method == "POST":
           user = request.user
           if user.is_authenticated:
            movie = Movie.objects.get(slug=slug)
            comment = request.POST.get('comment')
            UserReview.objects.create(
                user=user, movie=movie, comment=comment
            )

    reviews = UserReview.objects.filter(movie=movie).order_by('-id')
    context = {
        'movie': movie,
        'reviews': reviews
    }   
    return render(request, 'movie-watching.html', context=context)


def blog(request):
    return render(request, 'blog.html')

def categories(request):
    return render(request, 'categories.html')