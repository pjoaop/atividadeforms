from django.shortcuts import render
from main.forms import *
# Create your views here.

def cadastro_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            form = PessoaForm()
    else:
        form = PessoaForm()

    return render(request,'form.html', { 'form' : form })