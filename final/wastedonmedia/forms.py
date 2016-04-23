from django.forms import ModelForm
from models import *


class FilmForm(ModelForm):
    class Meta:
        model = Film
        exclude = ()

class SerieForm(ModelForm):
    class Meta:
        model = Series
        exclude = ()

class SongForm(ModelForm):
    class Meta:
        model = Song
        exclude = ()
