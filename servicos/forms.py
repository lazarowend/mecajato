from django.forms import ModelForm
from .models import Servico, CategoriaManutenção

class FormServico(ModelForm):
    class Meta:
        model = Servico
        exclude = ['finalizado', 'protocolo']
        #fields = ['']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': str(field).capitalize().replace('_', ' ')})
        
        choices = []
        for i, j in self.fields['categoria_manutencao'].choices:
            categoria = CategoriaManutenção.objects.get(titulo=j)
            choices.append((i.value ,categoria.get_titulo_display()))

        self.fields['categoria_manutencao'].choices = choices

class FormCategoriaManutenção(ModelForm):
    pass