from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_veiculos, name='listar_veiculos'),
    path('novo/', views.criar_veiculo, name='criar_veiculo'),
    path('<int:id>/', views.detalhar_veiculo, name='detalhar_veiculo'),
    path('<int:id>/editar/', views.editar_veiculo, name='editar_veiculo'),
    path('<int:id>/excluir/', views.excluir_veiculo, name='excluir_veiculo'),
]
