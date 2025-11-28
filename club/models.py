# club/models.py

from django.db import models

# ----------------------------------------------------
# 1. Modelo de Posición (Position)
# ----------------------------------------------------
# Define el rol específico de la persona (Ej: 'Delantero', 'Tesorero', 'Entrenador').
class Position(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la Posición")
    
    class Meta:
        verbose_name = "Posición"
        verbose_name_plural = "Posiciones"
        
    def __str__(self):
        return self.name

# ----------------------------------------------------
# 2. Modelo de Categoría (Category)
# ----------------------------------------------------
# Define el grupo al que pertenece la persona (Ej: 'Fútbol Masculino Mayor', 'Comisión Directiva').
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la Categoría")
    
    class Meta:
        verbose_name = "Categoría (Plantel/Área)"
        verbose_name_plural = "Categorías (Planteles/Áreas)"
        
    def __str__(self):
        return self.name

# ----------------------------------------------------
# 3. Modelo de Persona (Person)
# ----------------------------------------------------
# Modelo unificado para Jugadores, Entrenadores, y Directivos.
class Person(models.Model):

    # La relación M2M ahora va a través del modelo ClubRole
    roles = models.ManyToManyField(
        'Category', 
        through='ClubRole', 
        related_name='staff_members',
        verbose_name="Roles/Áreas Asignadas"
    )
    
    full_name = models.CharField(max_length=150, verbose_name="Nombre Completo")
    
    # Útil para jugadores, no aplica para directivos (null=True, blank=True).
    jersey_number = models.IntegerField(
        null=True, 
        blank=True, 
        verbose_name="Número de Camiseta"
    )
    
    # Foto de la persona. Se guardará en /media/club/
    photo = models.ImageField(
        upload_to='club/photos/', 
        null=True, 
        blank=True, 
        verbose_name="Foto"
    )
    
    # Campo para ordenar a las personas dentro de su categoría (Ej: Primero el arquero, luego defensas).
    order = models.IntegerField(default=0, verbose_name="Orden de Visualización")
    
    # Determina si la persona debe mostrarse en la web.
    is_active = models.BooleanField(default=True, verbose_name="Activo/Visible")

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering = ['full_name']
        
    def __str__(self):
        return self.full_name

# ----------------------------------------------------
# 4. Modelo Intermediario (ClubRole)
# ----------------------------------------------------
# Define el rol específico que una PERSONA tiene DENTRO de una CATEGORÍA.
class ClubRole(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name="Persona")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoría (Equipo/Área)")
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Rol Específico")
    
    # Campo para ordenar a la persona dentro de ESA categoría/rol (Ej: Capitán primero).
    order = models.IntegerField(default=0, verbose_name="Orden en la Categoría")
    
    class Meta:
        verbose_name = "Rol de Club"
        verbose_name_plural = "Roles de Club"
        # Asegura que una persona no pueda tener el mismo rol en la misma categoría dos veces.
        unique_together = ('person', 'category', 'position')
        ordering = ['category', 'order']
        
    def __str__(self):
        return f"{self.person.full_name} como {self.position.name} en {self.category.name}"