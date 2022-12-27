"""models from app musica"""
from django.db import models

# Songs -> precisa conter a musica e o artista
class Musica(models.Model):
    """define songs and artist for user can insert"""
    nome = models.CharField(max_length=50)
    artista = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


# Playlist -> músicas e artistas selecionadas pelo usuário herdando os dois em uma lista
