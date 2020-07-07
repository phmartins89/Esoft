from  django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('endereco', views.cadastro_endereco, name='endereco'),
    path('cadastrar-endereco', views.cadastro_endereco, name= 'cadastro_endereco'),
    path('recuperar-endereco', views.recuperar_endereco, name= 'recuperar_endereco')
]