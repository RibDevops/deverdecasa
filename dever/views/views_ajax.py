from django.http import JsonResponse
from ..models import Professor, Materia, Livro

def get_professores_by_escola(request, escola_id):
    professores = Professor.objects.filter(fk_escola_id=escola_id)
    data = [{'id': prof.id, 'nome': prof.nome_professor} for prof in professores]
    return JsonResponse(data, safe=False)

def get_materia_by_professor(request, professor_id):
    professor = Professor.objects.get(id=professor_id)
    materia = {'id': professor.fk_materia.id, 'nome': professor.fk_materia.nome_materia}
    return JsonResponse(materia)

def get_livros_by_materia(request, materia_id):
    livros = Livro.objects.filter(fk_materia_id=materia_id)
    data = [{'id': livro.id, 'nome': livro.nome_livro} for livro in livros]
    return JsonResponse(data, safe=False)
