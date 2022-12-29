"""arquivo serializador da aplicação musica"""
from rest_framework import serializers
from .models import Musica, Playlist


class MusicaSerializer(serializers.ModelSerializer):
    """class serializadora do models Musica"""
    class Meta:
        """Class meta"""
        model = Musica
        fields = ['id', 'nome', 'artista']


class PlaylistSerializer(serializers.ModelSerializer):
    """class serializadora do models Playlist"""
    class Meta:
        """Class meta"""
        model = Playlist
        fields = ['id', 'nome', 'musica']
