from django.forms import ModelForm
from .models import Pessoa, Pertence

class FormPessoa(ModelForm):

    class Meta:
        model = Pessoa
        fields = ('nome_pessoa', 'endereco', 'cpf')

class FormPertence(ModelForm):

    class Meta:
        model = Pertence
        fields = ('nome_pertence', 'descricao')