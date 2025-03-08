
from django.urls import path
from .views import FloorCreateView, FloorListView



app_name = 'organizational-structure' 
urlpatterns = [
    path('floor/create/', FloorCreateView.as_view(), name='floor_create'),
    path('floor/list/', FloorListView.as_view(), name='floor_list'),
    # Otras URLs
]