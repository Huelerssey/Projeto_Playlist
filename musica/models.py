"""models do app musica"""
from django.db import models


class Artista(models.Model):
    """
    Define os artistas que um usuário pode inserir.

    param: nome: str
    """
    nome = models.CharField(max_length=50)
    _dt_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Define o nome do banco de dados e a string no plural"""
        db_table = 'artist'
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'

    def __str__(self):
        return str(self.nome)


class Musica(models.Model):
    """
    define musicas que um usuário pode inserir.

    param: nome: str
    param: artista: chave estrangeira
    """
    nome = models.CharField(max_length=50)
    artista = models.ForeignKey("Artista", on_delete=models.CASCADE)
    _dt_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Define o nome do banco de dados e a string no plural"""
        db_table = 'music'
        verbose_name = 'Music'
        verbose_name_plural = 'Musics'

    def __str__(self):
        return str(self.nome)


class Playlist(models.Model):
    """
    Permite ao usuário organizar as músicas e artistas.

    param: nome: str
    param: musicas: chave estrangeira
    """
    nome = models.CharField(max_length=50)
    musicas = models.ManyToManyField("Musica")
    _dt_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Define o nome do bando de dados e a string no plural"""
        db_table = 'playlist'
        verbose_name = 'Playlist'
        verbose_name_plural = 'playlists'

    def __str__(self):
        return str(self.nome)
