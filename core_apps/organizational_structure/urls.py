
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
    # Cargos
    path("positions/", PositionListView.as_view(), name="positions_list"),
    path("positions/create/", PositionCreateView.as_view(), name="positions_create"),
    path("positions/edit/<uuid:pk>/", PositionUpdateView.as_view(), name="positions_edit"),
    path("positions/delete/<uuid:pk>/", PositionDeleteView.as_view(), name="positions_delete"),
    # Custodias
    path("custodians/", CustodianListView.as_view(), name="custodians_list"),
    path("custodians/create/", CustodianCreateView.as_view(), name="custodians_create"),
    path("custodians/edit/<uuid:pk>/", CustodianUpdateView.as_view(), name="custodians_edit"),
    path("custodians/delete/<uuid:pk>/", CustodianDeleteView.as_view(), name="custodians_delete"),
]