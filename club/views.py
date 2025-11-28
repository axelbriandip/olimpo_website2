# club/views.py

from django.views.generic import TemplateView
from .models import Person, Category # Importamos Category

# --- Función Auxiliar para Filtrado ---
def _get_club_data_by_category_name(category_name):
    """Filtra y agrupa personas por el nombre de la categoría."""
    try:
        # Intenta obtener la Categoría por el nombre (case-insensitive)
        category = Category.objects.get(name__iexact=category_name)
    except Category.DoesNotExist:
        return None # Devuelve None si la categoría no existe

    # Filtra Personas que están en esa Categoría
    people = Person.objects.filter(
        clubrole__category=category, 
        is_active=True
    ).prefetch_related(
        'clubrole_set__position', 
        'clubrole_set__category'
    ).order_by('clubrole__order') 
    
    return {
        'category': category,
        'people': people
    }

# ----------------------------------------------------
# 1. VISTA DE PLANTELES DEPORTIVOS (Mantiene la lógica anterior)
# ----------------------------------------------------
class PlayerListView(TemplateView):
    template_name = 'club/player_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Filtra categorías que NO sean 'Comisión Directiva' (asumiendo que las deportivas tienen otras palabras)
        # Esto requiere que tus categorías deportivas NO se llamen 'Comisión Directiva'.
        sport_categories = Category.objects.exclude(name__iexact='Comisión Directiva').order_by('id')
        
        club_data = []
        for cat in sport_categories:
            people = Person.objects.filter(
                clubrole__category=cat, 
                is_active=True
            ).prefetch_related(
                'clubrole_set__position', 
                'clubrole_set__category'
            ).order_by('clubrole__order')
            
            if people:
                club_data.append({
                    'category': cat,
                    'people': people
                })
        
        context['club_data'] = club_data
        context['page_title'] = 'Planteles Deportivos'
        return context


# ----------------------------------------------------
# 2. VISTA DE COMISIÓN DIRECTIVA (Filtro Exacto)
# ----------------------------------------------------
class BoardView(TemplateView):
    template_name = 'club/board_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Filtra solo por la categoría exacta 'Comisión Directiva'
        data = _get_club_data_by_category_name('Comisión Directiva')
        
        context['club_data'] = [data] if data else []
        context['page_title'] = 'Comisión Directiva'
        return context


# ----------------------------------------------------
# 3. VISTA DE HISTORIA (Placeholder, usará el nuevo módulo después)
# ----------------------------------------------------
class HistoryView(TemplateView):
    template_name = 'core/history.html' # Usaremos una plantilla genérica en 'core' por ahora
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Nuestra Historia'
        return context