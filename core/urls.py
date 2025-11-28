# core/urls.py

from django.urls import path
from . import views
from club.views import HistoryView # Importamos la vista que creamos en club/views.py

urlpatterns = [
    path('', views.home, name='home'),
    # Nueva ruta para Historia
    path('history/', HistoryView.as_view(), name='history'), 
]