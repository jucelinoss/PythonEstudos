from django.urls import path
from .views import index, contato, cliente

urlpatterns = [
    path('', index),
    path('contato', contato),
    path('cliente/<int: pk>', cliente, name='cliente')
    # /contato -> a barra é desnecessária
]