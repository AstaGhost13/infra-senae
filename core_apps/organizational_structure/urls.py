
from django.urls import path
from .views import *



app_name = 'organizational-structure' 
urlpatterns = [
    path('floor/create/', FloorCreateView.as_view(), name='floor_create'),
    path('floor/list/', FloorListView.as_view(), name='floor_list'),
    path('floor/edit/<uuid:pk>/', FloorUpdateView.as_view(), name='floor_edit'),  # Editar piso
    path('floor/delete/<uuid:pk>/', FloorDeleteView.as_view(), name='floor_delete'),  # Eliminar piso
    # Otras URLs
]