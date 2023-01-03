"""urls do projeto playlist CRUD"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from musica.views import MusicaViewSet, PlaylistViewSet, ArtistaViewSet


router = routers.DefaultRouter()
router.register(r'musicas', MusicaViewSet)
router.register(r'playlists', PlaylistViewSet)
router.register(r'artistas', ArtistaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
