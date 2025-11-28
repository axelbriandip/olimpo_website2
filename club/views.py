# club/views.py

from django.views.generic import TemplateView, ListView
from .models import Person, Category # Importamos los modelos de Club

# ----------------------------------------------------
# VISTA DE LISTADO DE PLANTELES (PlayerListView)
# ----------------------------------------------------
# Usamos TemplateView, pero sobrescribimos get_context_data 
# para manipular los datos de manera específica (agrupación).
class PlayerListView(TemplateView):
    template_name = 'club/player_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # 1. Obtener todas las categorías activas.
        categories = Category.objects.all().order_by('id')
        
        club_data = []
        for cat in categories:
            # 💡 CORRECCIÓN: Filtramos a través de la relación inversa del modelo ClubRole (que se llama clubrole_set por defecto)
            # o, en este caso, usamos la sintaxis de doble guion bajo para acceder al campo 'category' del modelo ClubRole.
            people = Person.objects.filter(
                clubrole__category=cat, 
                is_active=True
            ).prefetch_related(
                # ✅ Carga el modelo intermediario y la Posición relacionada
                'clubrole_set__position', 
                'clubrole_set__category'
            ).order_by('clubrole__order')
            
            if people:
                club_data.append({
                    'category': cat,
                    'people': people
                })
        
        context['club_data'] = club_data
        return context