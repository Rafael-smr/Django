from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    '''Cria o formulário para o modelo Task'''
    class Meta:
        model = Task
        fields = ['title', 'descriptions', 'completed']
        