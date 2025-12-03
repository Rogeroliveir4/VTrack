from django import forms
from .models import Veiculo

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ["placa", "modelo", "marca", "ano", "cor", "status"]

        widgets = {
            "status": forms.Select(attrs={"class": "select select-bordered w-full"})
        }
