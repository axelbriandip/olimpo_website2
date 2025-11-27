# core/views.py

from django.shortcuts import render

# Vista principal (Home Page).
def home(request):
    context = {
        # Puedes pasar datos específicos para la home aquí.
    }
    return render(request, 'core/home.html', context)