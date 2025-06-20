from django.db import models

class Task(models.Model):
    '''Cria o modelo de tarefas'''
    title = models.CharField(max_length=100)
    descriptions = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        '''Retorna uma representação em string do modelo'''
        return self.title, self.description, self.completed