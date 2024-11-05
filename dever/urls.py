# from django.urls import path
# from .views import DeverListView, DeverDetailView, DeverCreateView

# urlpatterns = [
#     path('deveres/', DeverListView.as_view(), name='dever_list'),
#     path('dever/<int:pk>/', DeverDetailView.as_view(), name='dever_detail'),
#     path('dever/criar/', DeverCreateView.as_view(), name='dever_create'),
# ]


# dever/urls.py

from django.urls import path
from .views import DeverListView, DeverDetailView, DeverCreateView, DeverUpdateView, DeverDeleteView

urlpatterns = [
    path('', DeverListView.as_view(), name='dever_list'),
    path('<int:pk>/', DeverDetailView.as_view(), name='dever_detail'),
    path('novo/', DeverCreateView.as_view(), name='dever_create'),
    path('<int:pk>/editar/', DeverUpdateView.as_view(), name='dever_update'),
    path('<int:pk>/deletar/', DeverDeleteView.as_view(), name='dever_delete'),
]
