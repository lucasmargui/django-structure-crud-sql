from django.urls import path
from . import views

urlpatterns = [
    path('', views.material_list, name='material_list'),
    path('<int:pk>/', views.material_detail, name='material_detail'),
    path('new/', views.material_create, name='material_create'),
    path('<int:pk>/edit/', views.material_update, name='material_update'),
    path('<int:pk>/delete/', views.material_delete, name='material_delete'),
    path('order/list', views.order_list, name='order_list'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
    path('order/new/', views.order_create, name='order_create'),
    path('order/<int:pk>/edit/', views.order_update, name='order_update'),
    path('order/<int:pk>/delete/', views.order_delete, name='order_delete'),
]






