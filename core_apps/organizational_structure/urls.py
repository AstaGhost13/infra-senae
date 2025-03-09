
from django.urls import path
from .views import *



app_name = 'organizational_structure' 
urlpatterns = [
    # Pisos
    path('floor/create/', FloorCreateView.as_view(), name='floor_create'),
    path('floor/list/', FloorListView.as_view(), name='floor_list'),
    path('floor/edit/<uuid:pk>/', FloorUpdateView.as_view(), name='floor_edit'),  
    path('floor/delete/<uuid:pk>/', FloorDeleteView.as_view(), name='floor_delete'),  
    # Departamentos
    path('departments/list/', DepartmentListView.as_view(), name='departments_list'),  
    path('department/create/', DepartmentCreateView.as_view(), name='add_department'),
    path('department/edit/<uuid:pk>/', DepartmentUpdateView.as_view(), name='edit_department'),
    path('department/delete/<uuid:pk>/', DepartmentDeleteView.as_view(), name='delete_department'),
    # Posiciones
    path("positions/", PositionListView.as_view(), name="positions_list"),
    path("positions/create/", PositionCreateView.as_view(), name="positions_create"),
    path("positions/edit/<uuid:pk>/", PositionUpdateView.as_view(), name="positions_edit"),
    path("positions/delete/<uuid:pk>/", PositionDeleteView.as_view(), name="positions_delete"),
]