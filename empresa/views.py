from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Empresa

@cache_page(60)
def home(request):
    resultado = 0
    for _ in range(500000):
        # Alguma tarefa simples que leva tempo
        resultado += 2 * 3
    empresas = Empresa.objects.all()
    return render(request, 'home.html', context={'empresas':empresas})
