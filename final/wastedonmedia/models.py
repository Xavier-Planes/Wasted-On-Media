from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models	import User
from django.core.urlresolvers import reverse
from datetime import date

# Create your models here.

class Film(models.Model):
    name = models.TextField(unique=True, primary_key=True)
    director = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    trailer = models.URLField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    duration = models.TextField(blank=True, null=True)
    genre = models.TextField(blank=True, null=True)
    synopsis = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="media", blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('wastedonmedia:films_detail', kwargs={'pk': self.pk})


class Series(models.Model):
    name = models.TextField(unique=True, primary_key=True)
    director = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    trailer = models.URLField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    duration = models.TextField(blank=True, null=True)
    season = models.IntegerField(blank=True, null=True)
    chapters = models.IntegerField(blank=True, null=True)
    genre = models.TextField(blank=True, null=True)
    synopsis = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="media", blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('wastedonmedia:series_detail', kwargs={'pk': self.pk})


class Song(models.Model):
    name = models.TextField(unique=True, primary_key=True)
    group = models.TextField(blank=True, null=True)
    album = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    duration = models.TextField(blank=True, null=True)
    genre = models.TextField(blank=True, null=True)
    song_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="media", blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('wastedonmedia:songs_detail', kwargs={'pk': self.pk})