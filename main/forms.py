from django import forms
from main.models import Pessoa

class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields= '__all__'
