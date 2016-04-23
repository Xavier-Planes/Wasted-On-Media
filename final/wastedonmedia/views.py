from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from django.views.generic.base import TemplateResponseMixin
from django.core import serializers
from django.views.generic.edit import CreateView
from models import *
from forms import *
# Create your views here.


def mainpage(request):
    return render(request, 'wastedonmedia/mainpage.html')


class FilmsList(ListView):
    model = Film
    queryset = Film.objects.all()
    context_object_name = 'films'
    template_name = 'wastedonmedia/films_list.html'


class SeriesList(ListView):
    model = Series
    queryset = Series.objects.all()
    context_object_name = 'series'
    template_name = 'wastedonmedia/series_list.html'


class SongsList(ListView):
    model = Song
    queryset = Song.objects.all()
    context_object_name = 'songs'
    template_name = 'wastedonmedia/songs_list.html'


class FilmsDetail(DetailView):
    model = Film
    template_name = 'wastedonmedia/films_detail.html'


class SeriesDetail(DetailView):
    model = Series
    template_name = 'wastedonmedia/series_detail.html'


class SongsDetail(DetailView):
    model = Song
    template_name = 'wastedonmedia/songs_detail.html'


class FilmCreate(CreateView):
    model = Film
    template_name = 'wastedonmedia/form.html'
    form_class = FilmForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FilmCreate, self).form_valid(form)


class SeriesCreate(CreateView):
    model = Series
    template_name = 'wastedonmedia/form.html'
    form_class = SerieForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SeriesCreate, self).form_valid(form)


class SongCreate(CreateView):
    model = Song
    template_name = 'wastedonmedia/form.html'
    form_class = SongForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SongCreate, self).form_valid(form)