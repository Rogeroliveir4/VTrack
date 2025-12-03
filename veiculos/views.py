from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Veiculo
from .forms import VeiculoForm

def listar_veiculos(request):
    search = request.GET.get("search", "")
    veiculos = Veiculo.objects.all()

    if search:
        veiculos = veiculos.filter(
            Q(placa__icontains=search) |
            Q(modelo__icontains=search) |
            Q(marca__icontains=search)
        )

    return render(request, "veiculos/listar.html", {"veiculos": veiculos})


def criar_veiculo(request):
    form = VeiculoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("listar_veiculos")

    return render(request, "veiculos/criar.html", {"form": form})


def detalhar_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    return render(request, "veiculos/detalhes.html", {"veiculo": veiculo})


def editar_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("listar_veiculos")

    return render(request, "veiculos/editar.html", {"form": form, "veiculo": veiculo})


def excluir_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    veiculo.delete()
    return redirect("listar_veiculos")
