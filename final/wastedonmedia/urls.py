from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from models import *
from views import *

urlpatterns = [

    url(r'^films/$',
        FilmsList.as_view(),
        name='films_list'),

    url(r'^series/$',
        SeriesList.as_view(),
        name='series_list'),

    url(r'^songs/$',
        SongsList.as_view(),
        name='songs_list'),

    url(r'^film/(?P<pk>[a-zA-Z0-9 ]+)/$',
        FilmsDetail.as_view(),
        name='films_detail'),

    url(r'^serie/(?P<pk>[a-zA-Z0-9 ]+)/$',
        SeriesDetail.as_view(),
        name='series_detail'),

    url(r'^song/(?P<pk>[a-zA-Z0-9 ]+)/$',
        SongsDetail.as_view(),
        name='songs_detail'),

    url(r'^films/create/$',
        FilmCreate.as_view(),
        name='films_create'),

    url(r'^series/create/$',
        SeriesCreate.as_view(),
        name='series_create'),

    url(r'^songs/create/$',
        SongCreate.as_view(),
        name='songs_create'),
]