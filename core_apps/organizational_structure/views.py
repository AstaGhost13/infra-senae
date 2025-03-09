from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.edit import *
from django.views.generic import ListView
from .models import Floor
from .forms import FloorForm
# Create your views here.

#  Vista basada en clases
class FloorCreateView(CreateView):
    model = Floor
    form_class = FloorForm
    template_name = 'organizational_structure/floor_form.html'  # Ruta corregida
    success_url = reverse_lazy('organizational-structure:floor_list')  # Usa el namespace

class FloorListView(ListView):
    model = Floor
    template_name = 'organizational_structure/floor_list.html'  # Ruta corregida
    context_object_name = 'floors'  # Nombre del objeto en la plantilla


    # Vista para editar un piso
class FloorUpdateView(UpdateView):
    model = Floor
    form_class = FloorForm
    template_name = 'organizational_structure/floor_form.html'
    success_url = reverse_lazy('organizational-structure:floor_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Floor, id=self.kwargs['pk'])

# Vista para eliminar un piso
class FloorDeleteView(DeleteView):
    model = Floor
    template_name = 'organizational_structure/floor_confirm_delete.html'  # Plantilla de confirmación
    success_url = reverse_lazy('organizational-structure:floor_list')
class FloorCreateView(CreateView):
    model = Floor
    form_class = FloorForm
    template_name = 'organizational_structure/floor_form.html'
    success_url = reverse_lazy('organizational-structure:floor_list')