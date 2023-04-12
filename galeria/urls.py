# Essa página é criada no meu APP para eu sempre adicionar o caminho dos meus templates novos aqui.Faço a ligação dessa página com urls.py do projeto, nesse caso urls.py de setup

from django.urls import path

from galeria.views import index

urlpatterns = [
    path('', index),
]
