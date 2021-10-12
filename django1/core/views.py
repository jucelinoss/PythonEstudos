from django.shortcuts import render
from .models import Cliente


# Create your views here.
def index(request):
    clientes = Cliente.objects.all()
    for cliente in clientes:
        print(cliente.nome)

    context = {
        'curso': 'Programacao web com Dango Framework',
        'outro': 'Django é massa',
        'clientes': clientes
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')

# recomenda-se criar nomes de funcoes e objetos em ingles


#    if request.user == 'AnonymousUser':
#        status_usuario = 'usuário não logado'
#    else:
#        status_usuario = 'usuário logado'
#
