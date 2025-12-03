from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from openpyxl import Workbook

from .models import Motorista


# =========================================================
# LISTAR MOTORISTAS
# =========================================================
def listar_motoristas(request):
    q = request.GET.get("q", "")
    filtro = request.GET.get("filtro", "")

    motoristas = Motorista.objects.all()

    # Busca por nome ou CPF
    if q:
        motoristas = motoristas.filter(nome__icontains=q) | motoristas.filter(cpf__icontains=q)

    # FILTRO: ATIVOS
    if filtro == "ativos":
        motoristas = motoristas.filter(ativo=True)

    # FILTRO: INATIVOS
    if filtro == "inativos":
        motoristas = motoristas.filter(ativo=False)

    # FILTRO: CNH vencendo em até 40 dias
    if filtro == "vencendo":
        limite = timezone.now().date() + timezone.timedelta(days=40)
        motoristas = motoristas.filter(cnh_validade__lte=limite)

    return render(request, "motoristas/listar.html", {
        "motoristas": motoristas
    })


# =========================================================
# DETALHAR MOTORISTA
# =========================================================
def detalhar_motorista(request, id):
    motorista = get_object_or_404(Motorista, id=id)

    return render(request, "motoristas/detalhes.html", {
        "motorista": motorista
    })


# =========================================================
# CRIAR MOTORISTA
# =========================================================
def criar_motorista(request):
    if request.method == "POST":
        ativo = request.POST.get("ativo") == "on"

        Motorista.objects.create(
            nome=request.POST["nome"],
            cpf=request.POST["cpf"],
            telefone=request.POST["telefone"],
            email=request.POST["email"],
            cnh_numero=request.POST["cnh_numero"],
            cnh_categoria=request.POST["cnh_categoria"],
            cnh_validade=request.POST["cnh_validade"],
            ativo=ativo
        )

        return redirect("listar_motoristas")

    return render(request, "motoristas/form.html", {
        "titulo": "Novo Motorista",
        "motorista": {}
    })


# =========================================================
# EDITAR MOTORISTA
# =========================================================
def editar_motorista(request, id):
    motorista = get_object_or_404(Motorista, id=id)

    if request.method == "POST":
        motorista.nome = request.POST["nome"]
        motorista.cpf = request.POST["cpf"]
        motorista.telefone = request.POST["telefone"]
        motorista.email = request.POST["email"]
        motorista.cnh_numero = request.POST["cnh_numero"]
        motorista.cnh_categoria = request.POST["cnh_categoria"]
        motorista.cnh_validade = request.POST["cnh_validade"]
        motorista.ativo = request.POST.get("ativo") == "on"

        motorista.save()
        return redirect("listar_motoristas")

    return render(request, "motoristas/form.html", {
        "titulo": "Editar Motorista",
        "motorista": motorista
    })


# =========================================================
# EXCLUIR MOTORISTA
# =========================================================
def excluir_motorista(request, id):
    motorista = get_object_or_404(Motorista, id=id)
    motorista.delete()
    return redirect("listar_motoristas")


# =========================================================
# EXPORTAR MOTORISTAS PARA EXCEL
# =========================================================
def exportar_motoristas(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Motoristas"

    # Cabeçalhos
    ws.append(["Nome", "CPF", "Telefone", "Email", "CNH", "Categoria", "Validade", "Ativo"])

    # Dados
    for m in Motorista.objects.all():
        ws.append([
            m.nome,
            m.cpf,
            m.telefone,
            m.email,
            m.cnh_numero,
            m.cnh_categoria,
            m.cnh_validade.strftime("%d/%m/%Y"),
            "Sim" if m.ativo else "Não"
        ])

    # Resposta HTTP
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="motoristas.xlsx"'
    wb.save(response)
    return response
