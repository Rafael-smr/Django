from django.contrib import admin
from .models import Emprestimo

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('livro', 'usuario', 'data_emprestimo', 'data_devolucao_prevista', 'data_devolucao_real', 'status', 'multa')
    list_filter = ('status', 'data_emprestimo', 'data_devolucao_prevista')
    search_fields = ('livro__titulo', 'usuario__username')
    raw_id_fields = ('livro', 'usuario')

    def save_model(self, request, obj, form, change):
        if obj.data_devolucao_real and not obj.multa:
            obj.calcular_multa()
        super().save_model(request, obj, form, change)