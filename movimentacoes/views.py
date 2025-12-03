from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Movimentacao
from .forms import MovimentacaoForm

def listar_movimentacoes(request):
    search = request.GET.get("search", "")
    status = request.GET.get("status", "")

    movimentacoes = Movimentacao.objects.select_related("veiculo", "motorista").all()

    if search:
        movimentacoes = movimentacoes.filter(
            Q(veiculo__placa__icontains=search) |
            Q(motorista__nome__icontains=search)
        )

    if status:
        movimentacoes = movimentacoes.filter(status=status)

    return render(request, "movimentacoes/listar.html", {
        "movimentacoes": movimentacoes,
        "status": status,
        "search": search,
    })


def criar_movimentacao(request):
    form = MovimentacaoForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("listar_movimentacoes")

    return render(request, "movimentacoes/criar.html", {"form": form})


def detalhes_movimentacao(request, id):
    mov = get_object_or_404(Movimentacao, id=id)
    return render(request, "movimentacoes/detalhes.html", {"mov": mov})


def editar_movimentacao(request, id):
    mov = get_object_or_404(Movimentacao, id=id)
    form = MovimentacaoForm(request.POST or None, instance=mov)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("listar_movimentacoes")

    return render(request, "movimentacoes/editar.html", {"form": form, "mov": mov})


def excluir_movimentacao(request, id):
    mov = get_object_or_404(Movimentacao, id=id)
    mov.delete()
    return redirect("listar_movimentacoes")
