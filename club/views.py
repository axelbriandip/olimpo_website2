# club/views.py

from django.views.generic import TemplateView

# Vista placeholder para la lista de jugadores.
class PlayerListView(TemplateView):
    # La plantilla HTML que se usará.
    template_name = 'club/player_list.html' 
    # Aquí es donde se añadirán los modelos y la lógica después.