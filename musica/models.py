"""models do app musica"""
from django.db import models


class Base(models.Model):
    """
    Clase base que será herdada pelas demais classes

    param: nome: str
    param: dt_criacao: int
    """
    nome = models.CharField(max_length=50)
    dt_criacao = models.DateTimeField(auto_now_add=True)

# Artist -> precisa conter um ID que será relacionado a musica



# Songs -> precisa conter a musica e o artista
class Musica(Base):
    """
    define musicas e artistas que um usuário pode inserir

    param: artista: str
    """
    artista = models.CharField(max_length=50)

    class Meta:
        """Define o nome do bando de dados e a string no plural"""
        db_name = 'music'
        verbose_name = 'Music'
        verbose_name_plural = 'Musics'

    def __str__(self):
        return str(self.nome)


# Playlist -> músicas e artistas selecionadas pelo usuário herdando os dois em uma lista
class Playlist(Base):
    """
    Permite ao usuário organizar as músicas e artistas

    param: musica: id field
    """
    musica = models.ManyToManyField("Musica")

    class Meta:
        """Define o nome do bando de dados e a string no plural"""
        db_name = 'playlist'
        verbose_name = 'Playlist'
        verbose_name_plural = 'playlists'

    def __str__(self):
        return str(self.nome)
