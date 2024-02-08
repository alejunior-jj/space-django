from galeria.views import index, imagem
from django.urls import path


urlpatterns = [
    path('', index, name='home'),
    path('imagem/', imagem, name = 'imagem')
]

