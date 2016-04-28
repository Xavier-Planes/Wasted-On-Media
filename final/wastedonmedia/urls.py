from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, UpdateView
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
    
    url(r'^films/(?P<pk>[a-zA-Z0-9 ]+)/edit/$',
        UpdateView.as_view(
            model=Film,
            template_name='wastedonmedia/form.html',
            form_class=FilmForm),
        name='films_edit'),

    url(r'^series/(?P<pk>[a-zA-Z0-9 ]+)/edit/$',
        UpdateView.as_view(
            model=Series,
            template_name='wastedonmedia/form.html',
            form_class=SerieForm),
        name='series_edit'),

    url(r'^songs/(?P<pk>[a-zA-Z0-9 ]+)/edit/$',
        UpdateView.as_view(
            model=Song,
            template_name='wastedonmedia/form.html',
            form_class=SongForm),
        name='songs_edit'),

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
