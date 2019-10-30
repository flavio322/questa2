from django.contrib import admin

# Register your models here.
from .models import *

class AluguelAdmin(admin.ModelAdmin):
    list_display = ('data_festa','hora_inicio','hora_termino')
admin.site.register(Aluguel,AluguelAdmin)

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro','numero')
admin.site.register(Endereco,EnderecoAdmin)

class TemaAdmin(admin.ModelAdmin):
    list_display = ('nome','valor_aluguel')
admin.site.register(Tema,TemaAdmin)

class ItemTemaAdmin(admin.ModelAdmin):
    list_display = ('nome','descricao')
admin.site.register(ItemTema,ItemTemaAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','telefone')
admin.site.register(Cliente,ClienteAdmin)

