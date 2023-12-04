from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('fazendas/', views.exibir_fazendas, name='Fazendas'),
    path('areaplantio/', views.exibir_area, name='Área de Plantio'),
    path('talhoes/', views.exibir_talhoes, name='Talhões'),
    path('analisesolo/', views.exibir_analises, name='Análise de Solo'),
    path('cidades/', views.exibir_cidades, name='Cidades'),
    path('usuarios/', views.exibir_usuarios, name='Usuários'),
    path('exportadora/', views.exibir_exportadora, name='Exportadoras'),
    path('exportar_analises_csv/', views.exportar_analises_csv, name='exportar_analises_csv'),
]   
