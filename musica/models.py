"""models do app musica"""
from django.db import models

# Songs -> precisa conter a musica e o artista
class Musica(models.Model):
    """define musicas e artistas que um usuário pode inserir"""
    nome = models.CharField(max_length=50)
    artista = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


# Playlist -> músicas e artistas selecionadas pelo usuário herdando os dois em uma lista
class Playlist(models.Model):
    """Permite ao usuário organizar as músicas e artistas"""
    nome = models.CharField(max_length=50)
    musica = models.ManyToManyField("Musica")

    def __str__(self):
        return self.nome
