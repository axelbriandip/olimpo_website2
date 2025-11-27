# config/context_processors.py

from django.conf import settings

def global_settings(request):
    """Inyecta las variables CLUB_* de settings.py en el contexto de la plantilla."""
    return {
        'settings': settings
    }