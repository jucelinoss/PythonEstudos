from django.shortcuts import render
from website.models import AlunoUnivesp
from django.views.generic import ListView


def alunoUnivesp(request):
    alunos = AlunoUnivesp.objects.all()
    contexto = {'alunos': alunos}
    return render(request, "templates/alunosUnivesp.html", contexto)


class ListaAlunosUnivesp(ListView):
    template_name = "template/alunosUnivesp.html"
    model = AlunoUnivesp
    context_object_name = 'Alunos'
