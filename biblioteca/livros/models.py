from django.db import models

class Livro(models.Model):
    '''Modelo para representar um livro na biblioteca.'''
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    ano_publicado = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
