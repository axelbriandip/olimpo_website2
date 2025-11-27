# news/views.py

from django.views.generic import ListView, DetailView
from .models import Article, Category
from django.utils import timezone

# ----------------------------------------------------
# 1. VISTA DE LISTADO DE NOTICIAS (ArticleListView)
# ----------------------------------------------------
class ArticleListView(ListView):
    # El modelo de datos del que se obtendrán los objetos.
    model = Article
    # El nombre de la plantilla HTML que se usará para renderizar la lista.
    template_name = 'news/article_list.html'
    # La variable que contendrá la lista de artículos en la plantilla (por defecto es object_list).
    context_object_name = 'articles'
    # Paginación: Muestra 10 artículos por página (recomendado para performance).
    paginate_by = 10 

    # Sobreescribimos get_queryset para asegurar que solo se muestren 
    # los artículos publicados y cuya fecha de publicación haya pasado.
    def get_queryset(self):
        return Article.objects.filter(
            is_published=True,
            published_date__lte=timezone.now() # Publicados hasta ahora o en el pasado
        ).order_by('-published_date') # Los más nuevos primero

# ----------------------------------------------------
# 2. VISTA DE DETALLE DE NOTICIA (ArticleDetailView)
# ----------------------------------------------------
class ArticleDetailView(DetailView):
    # El modelo de datos.
    model = Article
    # El nombre de la plantilla HTML.
    template_name = 'news/article_detail.html'
    # La variable que contendrá el objeto (el artículo) en la plantilla (por defecto es object).
    context_object_name = 'article'

    # Sobreescribimos get_queryset para asegurarnos de que el detalle solo se pueda
    # ver si el artículo cumple con las condiciones de publicación, incluso si se accede 
    # directamente por ID. Si no se encuentra, dispara un 404.
    def get_queryset(self):
        return Article.objects.filter(
            pk=self.kwargs.get('pk'), # Filtra por la clave primaria de la URL
            is_published=True,
            published_date__lte=timezone.now()
        )