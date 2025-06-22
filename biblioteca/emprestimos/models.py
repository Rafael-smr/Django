from django.db import models
from livros.models import Livro
from usuarios.models import Usuario

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao_prevista = models.DateField()
    data_devolucao_real = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('emprestado', 'Emprestado'),
            ('devolvido', 'Devolvido'),
            ('atrasado', 'Atrasado'),
        ],
        default='emprestado'
    )
    multa = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Empréstimo de {self.livro.titulo} para {self.usuario.username}"

    def calcular_multa(self):
        from datetime import date
        if self.data_devolucao_real and self.data_devolucao_real > self.data_devolucao_prevista:
            dias_atraso = (self.data_devolucao_real - self.data_devolucao_prevista).days
            self.multa = dias_atraso * 1.00
            self.save()
            return self.multa
        return 0.00