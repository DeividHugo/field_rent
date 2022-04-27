from django.shortcuts import render

from .models import Cidade, Clube


# Create your views here.
def index(request):
    cidade = Cidade.objects.all()
    return render(request, 'web/index.html', {'cidade': cidade, 'coisa': 'Deivid'})
