from django.urls import path
from dever.views.views_ajax import *
from dever.views.views_dever import *
from dever.views import *
from django.urls import path
from . import views

app_name = 'dever' # Defina o namespace aqui

urlpatterns = [
    path('lista/', dever_list, name='dever_list'),
    path('<int:pk>/', dever_detail, name='dever_detail'),
    path('novo/', dever_create, name='dever_create'),
    path('<int:pk>/editar/', dever_update, name='dever_update'),
    path('<int:pk>/deletar/', dever_delete, name='dever_delete'),

    # Outras rotas
    path('ajax/get-professores/<int:escola_id>/', views.get_professores_by_escola, name='get_professores_by_escola'),
    path('ajax/get-materia/<int:professor_id>/', views.get_materia_by_professor, name='get_materia_by_professor'),
    path('ajax/get-livros/<int:materia_id>/', views.get_livros_by_materia, name='get_livros_by_materia'),

    # URLs para Escola
    path('escolas/', views.lista_escolas, name='lista_escolas'),
    path('escolas/nova/', views.cria_escolas, name='cria_escolas'),
    path('escolas/<pk>/atualiza/', views.atualiza_escolas, name='atualiza_escolas'),
    path('escolas/<pk>/deleta/', views.deleta_escolas, name='deleta_escolas'),

    # URLs para Turma
    path('turma/', views.lista_turma, name='lista_turma'),
    path('turma/nova/', views.cria_turma, name='cria_turma'),
    path('turma/<pk>/atualiza/', views.atualiza_turma, name='atualiza_turma'),
    path('turma/<pk>/deleta/', views.deleta_turma, name='deleta_turma'),

    #... (Adicione URLs para Materia, , , )
    # Exemplo para Materia:
    path('materia/', views.lista_materia, name='lista_materia'),
    path('materia/nova/', views.cria_materia, name='cria_materia'),
    path('materia/<pk>/atualiza/', views.atualiza_materia, name='atualiza_materia'),
    path('materia/<pk>/deleta/', views.deleta_materia, name='deleta_materia'),

    # Exemplo para professor:
    path('professor/', views.lista_professor, name='lista_professor'),
    path('professor/nova/', views.cria_professor, name='cria_professor'),
    path('professor/<pk>/atualiza/', views.atualiza_professor, name='atualiza_professor'),
    path('professor/<pk>/deleta/', views.deleta_professor, name='deleta_professor'),

    # Exemplo para livro:
    path('livro/', views.lista_livro, name='lista_livro'),
    path('livro/nova/', views.cria_livro, name='cria_livro'),
    path('livro/<pk>/atualiza/', views.atualiza_livro, name='atualiza_livro'),
    path('livro/<pk>/deleta/', views.deleta_livro, name='deleta_livro'),

    # Exemplo para aluno:
    path('alunos/', views.lista_alunos, name='lista_alunos'),
    path('alunos/nova/', views.cria_alunos, name='cria_alunos'),
    path('alunos/<pk>/atualiza/', views.atualiza_alunos, name='atualiza_alunos'),
    path('alunos/<pk>/deleta/', views.deleta_alunos, name='deleta_alunos'),
]


