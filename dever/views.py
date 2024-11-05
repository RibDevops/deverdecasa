
# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from django.views.generic import ListView, DetailView, CreateView
# from django.urls import reverse_lazy
# from django.http import HttpResponseForbidden
# from .models import Escola, Professor, Aluno, Materia, Livro, DeverDeCasa, User
# from .forms import DeverDeCasaForm








# class RoleRequiredMixin:
#     allowed_roles = []

#     def dispatch(self, request, *args, **kwargs):
#         if request.user.role not in self.allowed_roles:
#             return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
#         return super().dispatch(request, *args, **kwargs)

# @method_decorator(login_required, name='dispatch')
# class DeverListView(RoleRequiredMixin, ListView):
#     model = DeverDeCasa
#     template_name = "dever_list.html"
#     context_object_name = "deveres"
#     allowed_roles = [User.COORDENADOR, User.PROFESSOR, User.PAI]

#     def get_queryset(self):
#         if self.request.user.role == User.COORDENADOR:
#             return DeverDeCasa.objects.all()
#         elif self.request.user.role == User.PROFESSOR:
#             return DeverDeCasa.objects.filter(fk_professor__usuario=self.request.user)
#         elif self.request.user.role == User.PAI:
#             return DeverDeCasa.objects.all()
#         return DeverDeCasa.objects.none()

# @method_decorator(login_required, name='dispatch')
# class DeverDetailView(RoleRequiredMixin, DetailView):
#     model = DeverDeCasa
#     template_name = "dever_detail.html"
#     context_object_name = "dever"
#     allowed_roles = [User.COORDENADOR, User.PROFESSOR, User.PAI]

#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         if not self.object.is_accessible_by(request.user):
#             return HttpResponseForbidden("Você não tem permissão para acessar este dever.")
#         return super().get(request, *args, **kwargs)


# @method_decorator(login_required, name='dispatch')
# class DeverCreateView(RoleRequiredMixin, CreateView):
#     model = DeverDeCasa
#     form_class = DeverDeCasaForm
#     template_name = "dever_form.html"
#     success_url = reverse_lazy('dever_list')
#     allowed_roles = [User.COORDENADOR, User.PROFESSOR]

#     def form_valid(self, form):
#         if self.request.user.role == User.PROFESSOR:
#             form.instance.fk_professor = get_object_or_404(Professor, usuario=self.request.user)
#         return super().form_valid(form)


# dever/views.py

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import DeverDeCasa

class DeverListView(ListView):
    model = DeverDeCasa
    template_name = 'dever/dever_list.html'
    context_object_name = 'deveres'

class DeverDetailView(DetailView):
    model = DeverDeCasa
    template_name = 'dever/dever_detail.html'
    context_object_name = 'dever'

class DeverCreateView(CreateView):
    model = DeverDeCasa
    template_name = 'dever/dever_form.html'
    fields = ['fk_escola', 'fk_professor', 'fk_materia', 'fk_livro', 'dever']
    success_url = reverse_lazy('dever_list')

class DeverUpdateView(UpdateView):
    model = DeverDeCasa
    template_name = 'dever/dever_form.html'
    fields = ['fk_escola', 'fk_professor', 'fk_materia', 'fk_livro', 'dever']
    success_url = reverse_lazy('dever_list')

class DeverDeleteView(DeleteView):
    model = DeverDeCasa
    template_name = 'dever/dever_confirm_delete.html'
    success_url = reverse_lazy('dever_list')
