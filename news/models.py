# news/models.py

from django.db import models
from django.utils import timezone

# Modelo para clasificar las noticias (ej: "Fútbol Masculino", "Básquet", "Institucional").
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        
    def __str__(self):
        return self.name

# Modelo principal para las noticias del club.
class Article(models.Model):
    # La categoría de la noticia, relacionada con el modelo Category.
    # on_delete=models.CASCADE asegura que si se borra una categoría, se borran sus artículos.
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='articles', 
        verbose_name="Categoría"
    )
    
    title = models.CharField(max_length=200, verbose_name="Título")
    
    # Campo corto para la vista previa o el listado de noticias.
    summary = models.TextField(verbose_name="Resumen")
    
    # El cuerpo del texto completo. Usaremos un campo TextField simple por ahora.
    # Recomendación futura: Reemplazar con RichTextEditor (como CKEditor o TinyMCE)
    # para permitir formato (negrita, cursiva, etc.) de forma fácil para el administrador.
    body = models.TextField(verbose_name="Cuerpo del Artículo")
    
    # Imagen principal de la noticia. Se guardará en /media/news/
    image = models.ImageField(upload_to='news/images/', verbose_name="Imagen Principal")
    
    # Campo para la fecha de publicación.
    published_date = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Publicación")
    
    # Determina si el artículo debe mostrarse. Útil para borradores.
    is_published = models.BooleanField(default=False, verbose_name="Publicado")
    
    # Opcional: Campo para ordenar las noticias destacadas manualmente.
    highlight_order = models.IntegerField(default=0, verbose_name="Orden de Destacado")

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        # Ordena las noticias por fecha de publicación descendente (las más nuevas primero).
        ordering = ['-published_date', '-highlight_order']
        
    def __str__(self):
        return self.title