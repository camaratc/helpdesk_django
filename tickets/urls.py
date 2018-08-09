from django.urls import path

from . import views

app_name = 'tickets'

handler404 = views.erro_404

urlpatterns = [
    path('', views.home, name='home'),
    path('solicitar/', views.solicitar_suporte, name='solicitar_suporte'),
    path('solicitar/<str:codigo>', views.detalhes_solicitacao, name="detalhes_solicitacao"),
    path('buscar/', views.buscar_solicitacao, name="buscar_solicitacao"),
]
