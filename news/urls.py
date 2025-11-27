# news/urls.py

from django.urls import path
from .views import ArticleListView, ArticleDetailView

# Define el "namespace" para usar nombres de rutas únicos (ej: {% url 'news:list' %})
app_name = 'news' 

urlpatterns = [
    # Ruta: /news/
    # Nombre de la ruta: news:list
    path('', ArticleListView.as_view(), name='list'),
    
    # Ruta: /news/1/, /news/25/, etc. 
    # Se usa <int:pk> para capturar la clave primaria (ID) del artículo.
    # Nombre de la ruta: news:detail
    path('<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    
    # OPCIONAL: Si deseas listar por categoría (ej: /news/category/futbol/)
    # path('category/<slug:category_slug>/', views.CategoryListView.as_view(), name='by_category'),
]