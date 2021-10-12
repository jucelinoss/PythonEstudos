from django.contrib import admin
from .models import Produto, Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


# permite administrar cadastro dos modelos desejados
admin.site.register(Produto)
admin.site.register(Cliente, ClienteAdmin)
