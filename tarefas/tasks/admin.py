from django.contrib import admin
from tasks.models import Task

admin.site.register(Task)
'''Faz com q o admin possa manipular as Tasks do Models'''
