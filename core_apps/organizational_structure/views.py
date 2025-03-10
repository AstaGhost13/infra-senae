from django.contrib import messages
from django import forms
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.edit import *
from django.views.generic import ListView
from .models import Custodian, Department, Floor, Position
from .forms import CustodianForm, DepartmentForm, FloorForm, PositionForm
# Create your views here.

#  Vista basada en clases
class FloorCreateView(CreateView):
    model = Floor
    form_class = FloorForm
    template_name = 'organizational_structure/floor_form.html'  # Ruta corregida
    success_url = reverse_lazy('organizational_structure:floor_list')  # Usa el namespace

class FloorListView(ListView):
    model = Floor
    template_name = 'organizational_structure/floors_list.html'
    context_object_name = 'floors'
    paginate_by = 4  # Número de pisos por página

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        sort_field = self.request.GET.get("sort", "description")
        sort_order = self.request.GET.get("order", "asc")

        floors_list = Floor.objects.filter(status=True)

        if query:
            floors_list = floors_list.filter(description__icontains=query)

        if sort_order == "desc":
            sort_field = f"-{sort_field}"

        return floors_list.order_by(sort_field)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get("q", "")
        context['sort_field'] = self.request.GET.get("sort", "description").lstrip("-")
        context['sort_order'] = self.request.GET.get("order", "asc")
        return context



    # Vista para editar un piso
class FloorUpdateView(UpdateView):
    model = Floor
    form_class = FloorForm
    template_name = 'organizational_structure/floor_edit.html'
    success_url = reverse_lazy('organizational_structure:floor_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Floor, id=self.kwargs['pk'])

# Vista para eliminar un piso
class FloorDeleteView(DeleteView):
    model = Floor
    template_name = 'organizational_structure/floor_confirm_delete.html'  # Plantilla de confirmación
    success_url = reverse_lazy('organizational_structure:floor_list')
    
class DepartmentListView(ListView):
    model = Department
    template_name = "organizational_structure/departments_list.html"
    context_object_name = "departments"
    success_url = reverse_lazy('organizational_structure:floor_list')
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        sort_field = self.request.GET.get("sort", "description")
        sort_order = self.request.GET.get("order", "asc")
        
        departments = Department.objects.all()
        
        if query:
            departments = departments.filter(description__icontains=query)
        
        if sort_order == "desc":
            sort_field = f"-{sort_field}"
        departments = departments.order_by(sort_field)
        
        return departments

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        context["sort_field"] = self.request.GET.get("sort", "description").lstrip("-")
        context["sort_order"] = self.request.GET.get("order", "asc")
        return context

class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = "organizational_structure/departments_add.html"
    success_url = reverse_lazy("organizational_structure:departments_list")

    def form_valid(self, form):
        messages.success(self.request, "Departamento agregado correctamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Hubo un error al agregar el departamento.")
        return super().form_invalid(form)

class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = "organizational_structure/departments_edit.html"
    success_url = reverse_lazy("organizational_structure:departments_list")

    def form_valid(self, form):
        messages.success(self.request, "Departamento actualizado correctamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Hubo un error al actualizar el departamento.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["floors"] = Floor.objects.all()
        context["departments"] = Department.objects.all()
        return context
    def get_object(self, queryset=None):
        return get_object_or_404(Department, id=self.kwargs["pk"])

class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = "organizational_structure/delete_department.html"
    success_url = reverse_lazy("organizational_structure:department_list")

    def post(self, request, *args, **kwargs):
        department = self.get_object()
        department.status = False  # Desactivar el departamento
        department.save()
        messages.success(request, "El departamento ha sido desactivado correctamente.")
        return super().post(request, *args, **kwargs)

# Vista para listar los cargos

class PositionListView(ListView):
    model = Position
    template_name = "organizational_structure/positions_list.html"
    context_object_name = "positions"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        sort_field = self.request.GET.get("sort", "description")
        sort_order = self.request.GET.get("order", "asc")
        
        positions = Position.objects.filter(status=True)
        
        if query:
            positions = positions.filter(description__icontains=query)
        
        if sort_order == "desc":
            sort_field = f"-{sort_field}"
        positions = positions.order_by(sort_field)
        
        return positions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        context["sort_field"] = self.request.GET.get("sort", "description").lstrip("-")
        context["sort_order"] = self.request.GET.get("order", "asc")
        return context


class PositionCreateView(CreateView):
    model = Position
    form_class = PositionForm
    template_name = "organizational_structure/positions_add.html"
    success_url = reverse_lazy("organizational_structure:positions_list")

    def form_valid(self, form):
        messages.success(self.request, "Cargo creado correctamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Hubo un error al crear el cargo.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["departments"] = Department.objects.filter(status=True)
        return context



class PositionUpdateView(UpdateView):
    model = Position
    form_class = PositionForm
    template_name = "organizational_structure/positions_edit.html"
    success_url = reverse_lazy("organizational_structure:positions_list")

    def form_valid(self, form):
        messages.success(self.request, "Cargo actualizado correctamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Hubo un error al actualizar el cargo.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["departments"] = Department.objects.filter(status=True)
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Position, id=self.kwargs["pk"])



class PositionDeleteView(DeleteView):
    model = Position
    template_name = "organizational_structure/positions_confirm_delete.html"
    success_url = reverse_lazy("organizational_structure:positions_list")

    def post(self, request, *args, **kwargs):
        position = self.get_object()
        position.status = False  # Desactivar el cargo
        position.save()
        messages.success(request, "El cargo ha sido desactivado correctamente.")
        return super().post(request, *args, **kwargs)
    
# Vista para listar las custodias


class CustodianListView(ListView):
    model = Custodian
    template_name = "organizational_structure/custodians_list.html"
    context_object_name = "custodians"
    paginate_by = 10  # Número de custodios por página

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        sort_field = self.request.GET.get("sort", "first_name")
        sort_order = self.request.GET.get("order", "asc")

        custodians = Custodian.objects.filter(status=True)

        if query:
            custodians = custodians.filter(first_name__icontains=query)

        if sort_order == "desc":
            sort_field = f"-{sort_field}"
        
        return custodians.order_by(sort_field)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get("q", "")
        context['sort_field'] = self.request.GET.get("sort", "first_name").lstrip("-")
        context['sort_order'] = self.request.GET.get("order", "asc")
        return context
    
class CustodianCreateView(CreateView):
    model = Custodian
    form_class = CustodianForm
    template_name = "organizational_structure/custodians_add.html"
    success_url = reverse_lazy("organizational_structure:custodians_list")

    def form_valid(self, form):
        messages.success(self.request, "Custodio creado correctamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Hubo un error al crear el custodio.")
        return super().form_invalid(form)


class CustodianUpdateView(UpdateView):
    model = Custodian
    form_class = CustodianForm
    template_name = "organizational_structure/custodians_edit.html"
    success_url = reverse_lazy("organizational_structure:custodians_list")

    def form_valid(self, form):
        messages.success(self.request, "Custodio actualizado correctamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Hubo un error al actualizar el custodio.")
        return super().form_invalid(form)

    def get_object(self, queryset=None):
        return get_object_or_404(Custodian, id=self.kwargs["pk"])
    
class CustodianDeleteView(DeleteView):
    model = Custodian
    template_name = "organizational_structure/custodians_confirm_delete.html"
    success_url = reverse_lazy("organizational_structure:custodians_list")

    def post(self, request, *args, **kwargs):
        custodian = self.get_object()
        custodian.status = False  # Desactivar al custodio
        custodian.save()
        messages.success(request, "El custodio ha sido desactivado correctamente.")
        return super().post(request, *args, **kwargs)