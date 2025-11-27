# club/urls.py

from django.urls import path
from .views import PlayerListView # Importamos la vista que acabamos de crear

app_name = 'club'

urlpatterns = [
    # Ruta: /club/players/
    # Nombre de la ruta: club:players_list (Este es el nombre que tu plantilla estaba buscando)
    path('players/', PlayerListView.as_view(), name='players_list'), 
]