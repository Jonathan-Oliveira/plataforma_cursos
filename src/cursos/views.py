from django.shortcuts import render
from django.shortcuts import redirect
from .models import Curso, Aula


def home(request):
    if request.session.get('usuario'):
        cursos = Curso.objects.all()
        request_usuario = request.session.get('usuario')
        return render(request, 'home.html', {'cursos': cursos, 'request_usuario': request_usuario})
    else:
        return redirect('/auth/login/?status=2')


def curso(request, id):
    if request.session.get('usuario'):
        v_curso = Curso.objects.get(id=id)
        aulas = Aula.objects.filter(curso=v_curso)
        return render(request, 'curso.html', {'curso': v_curso, 'aulas': aulas})

    else:
        return redirect('/auth/login/?status=2')


def aula(request, id):
    if request.session.get('usuario'):
        aula = Aula.objects.get(id=id)
        return render(request, 'aula.html', {'aula': aula})
    else:
        return redirect('/auth/login/?status=2')
