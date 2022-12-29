"""urls do projeto playlist CRUD"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from musica.views import MusicaViewSet, PlaylistViewSet


router = routers.DefaultRouter()
router.register(r'musicas', MusicaViewSet)
router.register(r'playlists', PlaylistViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
