from .models import Movie


def movie_detail_slug(request):
    movie_detail_slug = Movie.objects.first().slug


    return {'movie_detail_slug': movie_detail_slug}