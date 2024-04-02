from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator,InvalidPage,EmptyPage
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Movie,Genre
from .forms import MovieForm


# Create your views here.
def home(request):
    movie=Movie.objects.all()
    paginator = Paginator(movie, 6)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        movies = paginator.page(page)
    except (EmptyPage, InvalidPage):
        movies = paginator.page(paginator.num_pages)
    return render(request,'home.html',{'movie':movie,'movies':movies})

def movie_detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,'movie_detail.html',{'movie':movie})

def movie_add(request):
    if request.method == 'POST':
        form = MovieForm(request.POST,request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('/')
    else:
        form = MovieForm()
    return render(request, 'movie_add.html', {'form': form})

def movie_update(request, id):
    movie = get_object_or_404(Movie, id=id)
    form = MovieForm(request.POST,request.FILES)
    if movie.user != request.user:
        raise PermissionDenied
    return render(request, 'movie_update.html', {'form':form})

def movie_delete(request, id):
    movie = get_object_or_404(Movie, id=id)
    if movie.user != request.user:
        raise PermissionDenied
    movie.delete()
    return redirect('/')





def movie_list_by_genre(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    movies = Movie.objects.filter(genre=genre)
    return render(request, 'movies_by_genre.html', {'genre': genre, 'movies': movies})
