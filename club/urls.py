# club/urls.py

from django.urls import path
from .views import PlayerListView, BoardView # Importamos las nuevas vistas
# Importaremos HistoryView después, ya que su URL no está en la app 'club'

app_name = 'club' 

urlpatterns = [
    # 1. Planteles Deportivos
    path('players/', PlayerListView.as_view(), name='players_list'), 
    
    # 2. Comisión Directiva (Nueva URL)
    path('board/', BoardView.as_view(), name='board_list'),
    
    # 3. Historia (La dejamos en la app 'core' o 'history' para ser más limpio, 
    # pero la pondremos en un 'Nuestra Historia' general para el menú)
]