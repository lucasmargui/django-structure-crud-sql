from django.urls import path
from . import views

urlpatterns = [
    path('', views.material_list, name='material_list'),
    path('material/<int:pk>/', views.material_detail, name='material_detail'),
    path('material/new/', views.material_create, name='material_create'),
    path('material/<int:pk>/edit/', views.material_update, name='material_update'),
    path('material/<int:pk>/delete/', views.material_delete, name='material_delete'),
]






