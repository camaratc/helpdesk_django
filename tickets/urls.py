from django.urls import path

from . import views

app_name = 'tickets'

urlpatterns = [
    path('', views.home, name='home'),
    path('solicitar/', views.solicitar_suporte, name='solicitar_suporte'),
    path('solicitar/<int:pk>', views.detalhes_solicitacao, name="detalhes_solicitacao"),
    path('buscar/', views.buscar_solicitacao, name="buscar_solicitacao"),
]