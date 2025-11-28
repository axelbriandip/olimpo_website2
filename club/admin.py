# club/admin.py

from django.contrib import admin
from .models import Category, Position, Person, ClubRole 

# ----------------------------------------------------
# Registro de Modelos de Datos Estáticos
# ----------------------------------------------------

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Campos a mostrar en la lista de Categorías
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    # Campos a mostrar en la lista de Posiciones/Roles
    list_display = ('name',)
    search_fields = ('name',)

# ----------------------------------------------------
# 1. Inline para el Modelo Intermediario (ClubRole)
# ----------------------------------------------------
# Permite editar los roles de una persona directamente en la página de edición de la Persona.
class ClubRoleInline(admin.TabularInline):
    model = ClubRole
    extra = 1 # Muestra un campo extra vacío para facilitar la adición de roles
    # Campos que se muestran en el formulario inline para definir un rol específico:
    fields = ('category', 'position', 'order')

# ----------------------------------------------------
# 2. Registro del Modelo Persona (PersonAdmin)
# ----------------------------------------------------
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    # Campos a mostrar en la lista principal de Personas
    list_display = (
        'full_name', 
        'display_roles', # Método personalizado para mostrar un resumen de los roles
        'is_active',
        'jersey_number', # Incluimos el número aquí, aunque no aplique a Directivos
    )
    
    # Filtros para la barra lateral
    # Usamos la sintaxis de doble guion bajo ('__') para filtrar a través del modelo ClubRole
    list_filter = ('clubrole__category', 'clubrole__position', 'is_active')
    search_fields = ('full_name',)
    
    # El Inline se agrega aquí para editar los roles
    inlines = [ClubRoleInline]
    
    # Definición de las secciones del formulario de edición/creación
    fieldsets = (
        (None, {
            'fields': ('full_name', 'photo', 'is_active', 'jersey_number')
        }),
        ('Relaciones y Roles (Definidos abajo)', {
            'fields': (), # Los roles se gestionan completamente en el Inline
        }),
    )

    # ----------------------------------------------------
    # Método para Mostrar Resumen de Roles en list_display
    # ----------------------------------------------------
    def display_roles(self, obj):
        """Muestra un resumen de los roles de la persona en la lista del Admin."""
        # Obtenemos todos los roles asociados y optimizamos la consulta.
        roles = obj.clubrole_set.all().select_related('category', 'position')
        
        # Formato: "Rol (Categoría) / Rol (Categoría)"
        return " / ".join([f"{r.position.name} ({r.category.name})" for r in roles])
    
    display_roles.short_description = 'Roles Múltiples'