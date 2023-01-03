"""Views from app music"""
from rest_framework import viewsets
from .models import Musica, Playlist, Artista
from .serializers import MusicaSerializer, PlaylistSerializer, ArtistaSerializer


class ArtistaViewSet(viewsets.ModelViewSet):
    """view que retorna a class Artista de models"""
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer


class MusicaViewSet(viewsets.ModelViewSet):
    """view que retorna a class Musica de models"""
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    """view que retorna a class Musica de models"""
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
