from django.shortcuts import render

from .models import Cidade, Clube


# Create your views here.
def index(request):
<<<<<<< HEAD
    cidades = Cidade.objects.all()
    clubes = Clube.objects.all()
    return render(request, 'web/index.html', {
        'cidades': cidades,
        'clubes': clubes
    })


def clube(request, clube_id):
    clube = Clube.objects.get(id=clube_id)
    return render(request, 'web/clube.html', {
        'clube': clube
    })
=======
    cidade = Cidade.objects.all()
    return render(request, 'web/index.html', {'cidade': cidade, 'coisa': 'Deivid'})
>>>>>>> 0c47fd46b6934b46aaaf3291c5edf8dde05cb55c
