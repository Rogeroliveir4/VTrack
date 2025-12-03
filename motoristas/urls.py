from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar_motoristas, name="listar_motoristas"),
    path("novo/", views.criar_motorista, name="criar_motorista"),
    path("<int:id>/editar/", views.editar_motorista, name="editar_motorista"),
    path("<int:id>/excluir/", views.excluir_motorista, name="excluir_motorista"),
    path("<int:id>/detalhes/", views.detalhar_motorista, name="detalhar_motorista"),
    path("exportar/", views.exportar_motoristas, name="exportar_motoristas"),
]
