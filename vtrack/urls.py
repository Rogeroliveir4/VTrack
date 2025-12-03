from django.contrib import admin
from django.urls import path, include
from core.views import login_view, dashboard_view  # ← IMPORTANTE

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', login_view, name='login'),

    path('', dashboard_view, name="dashboard"),

    path("__reload__/", include("django_browser_reload.urls")),

    path('veiculos/', include('veiculos.urls')),
    path('movimentacoes/', include('movimentacoes.urls')),
    path("motoristas/", include("motoristas.urls")),

]
