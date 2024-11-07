from django.urls import path
from .views import dever_list, dever_detail, dever_create, dever_update, dever_delete

urlpatterns = [
    path('', dever_list, name='dever_list'),
    path('<int:pk>/', dever_detail, name='dever_detail'),
    path('novo/', dever_create, name='dever_create'),
    path('<int:pk>/editar/', dever_update, name='dever_update'),
    path('<int:pk>/deletar/', dever_delete, name='dever_delete'),
]
