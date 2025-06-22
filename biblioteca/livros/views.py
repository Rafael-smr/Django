from django.shortcuts import render, redirect
from .form import LivroForm

def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm()
    return render(request, 'livros/cadastrar_livro.html', {'form':form})
