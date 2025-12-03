from django import forms
from .models import Movimentacao

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ["veiculo", "motorista", "status", "observacao"]

        widgets = {
            "observacao": forms.Textarea(attrs={"rows": 3}),
            "status": forms.Select(attrs={"class": "select select-bordered"}),
        }
