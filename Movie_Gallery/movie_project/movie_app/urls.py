from django.urls import path
from . import views
from .views import movie_list_by_genre

app_name='movie_app'

urlpatterns=[
    path('',views.home,name='home'),
    path('detail/<int:movie_id>',views.movie_detail,name='movie_detail'),
    path('add/',views.movie_add,name='movie_add'),
    path('update/<int:id>',views.movie_update,name='movie_update'),
    path('delete/<int:id>',views.movie_delete,name='movie_delete'),
    path('genre/<int:genre_id>/', views.movie_list_by_genre, name='movie_list_by_genre'),
]