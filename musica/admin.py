"""admin from app musica"""
from django.contrib import admin
from .models import Musica, Playlist, Artista

admin.site.register(Musica)
admin.site.register(Playlist)
admin.site.register(Artista)
