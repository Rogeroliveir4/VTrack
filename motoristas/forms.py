from django import forms
from .models import Motorista

class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = ["nome", "cpf", "telefone", "categoria_cnh", "validade_cnh"]

        widgets = {
            "validade_cnh": forms.DateInput(attrs={"type": "date"}),
        }
