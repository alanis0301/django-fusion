from django.contrib import admin

# Register your models here.
from .models import Cargo, Servico, Funcionario, Feature, Preco, Cliente


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo','ativo','modificado')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico','icone', 'ativo','modificado')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','cargo', 'ativo', 'modificado')

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('nome','bio', 'posicao')

@admin.register(Preco)
class PrecoAdmin(admin.ModelAdmin):
    list_display = ('nome','icone', 'bio', 'valor', 'ativo', 'modificado')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'feedback', 'cargo', 'ativo', 'modificado')