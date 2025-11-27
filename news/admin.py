# news/admin.py

from django.contrib import admin
from .models import Category, Article

# Personalización de la vista de Categoría en el Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Personalización de la vista de Artículo en el Admin
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # Campos a mostrar en la lista de artículos
    list_display = (
        'title', 
        'category', 
        'published_date', 
        'is_published', 
        'highlight_order'
    )
    
    # Campos por los cuales se puede filtrar la lista
    list_filter = ('category', 'is_published', 'published_date')
    
    # Campos por los cuales se puede buscar
    search_fields = ('title', 'summary', 'body')
    
    # Campos que se rellenarán automáticamente con el valor de otros campos
    # En este caso, el slug (url amigable) puede generarse si tuvieras un campo slug
    # prepopulated_fields = {'slug': ('title',)} 
    
    # Campos que el administrador puede editar directamente desde la lista de artículos.
    list_editable = ('is_published', 'highlight_order') 
    
    # Define la estructura de las secciones al editar un artículo
    fieldsets = (
        (None, {
            'fields': ('title', 'summary', 'body', 'category', 'image')
        }),
        ('Publicación y Control', {
            'fields': ('published_date', 'is_published', 'highlight_order'),
            # 'classes': ('collapse',), # Oculta esta sección por defecto
        }),
    )