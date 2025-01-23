from django.shortcuts import render, redirect
from .models import User, UserReview
from movies.models import Movie
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', context={'error': 'user allaqachon mavjud'})

        if password == confirm_password:
            User.objects.create_user(username=username, password=password)
            return redirect('login')

    
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user=user)
            return redirect('home')
    
        else:
            pass
    
    return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')



@login_required
def add_review(request , movie_slug):
    if request.method == 'POST':
        user = request.user
        movie = Movie.objects.get(slug=movie_slug)
        comment = request.POST.get('comment')
        UserReview.objects.create(
            user=user, movie=movie, comment=comment
        )

    return redirect('movie_detail' , movie_slug=movie_slug)

