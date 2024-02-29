from django.contrib import admin
from . import models


class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    min_num = 1
    extra = 0
    can_delete = True


class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
        VariacaoInline
    ]


admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Variacao)
