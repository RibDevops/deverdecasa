from django.urls import path
from dever.views.views_ajax import *
from dever.views.views_dever import *
from django.urls import path
from . import views

urlpatterns = [
    path('', dever_list, name='dever_list'),
    path('<int:pk>/', dever_detail, name='dever_detail'),
    path('novo/', dever_create, name='dever_create'),
    path('<int:pk>/editar/', dever_update, name='dever_update'),
    path('<int:pk>/deletar/', dever_delete, name='dever_delete'),

    # Outras rotas
    path('ajax/get-professores/<int:escola_id>/', views.get_professores_by_escola, name='get_professores_by_escola'),
    path('ajax/get-materia/<int:professor_id>/', views.get_materia_by_professor, name='get_materia_by_professor'),
    path('ajax/get-livros/<int:materia_id>/', views.get_livros_by_materia, name='get_livros_by_materia'),
]


