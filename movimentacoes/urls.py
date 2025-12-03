from django.urls import path
from . import views 

urlpatterns = [
    path('', views.listar_movimentacoes, name='listar_movimentacoes'),
    path('nova/', views.criar_movimentacao, name='criar_movimentacao'),
    path('<int:id>/', views.detalhes_movimentacao, name='detalhes_movimentacao'),
    path('<int:id>/editar/', views.editar_movimentacao, name='editar_movimentacao'),
    path('<int:id>/excluir/', views.excluir_movimentacao, name='excluir_movimentacao'),


]
