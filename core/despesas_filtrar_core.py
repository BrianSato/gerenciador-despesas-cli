from datetime import datetime
from core.despesas_arquivo_core import carregar_despesas

def filtrar_por_categoria(categoria):
    despesas = carregar_despesas()

    return[
        despesa for despesa in despesas
        if despesa.get("categoria") == categoria
    ]

def filtrar_por_periodo(data_inicio, data_fim):
    despesas = carregar_despesas()

    data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date()
    data_fim = datetime.strptime(data_fim,"%Y-%m-%d").date()

    resultado = []
    for despesa in despesas:
        if "data" in despesa:
            data_despesa = datetime.strptime(despesa["data"],"%Y-%m-%d").date()
            if data_inicio <= data_despesa <= data_fim:
                resultado.append(despesa)
    return resultado


def filtrar_ano_selecionado(ano):  # Funcao onde se pega todas as despesas do ano selecionado
    despesas = carregar_despesas()

    return [
        d for d in despesas
        if d.get("data") and int(d["data"].split("-")[0]) == int(ano)
    ]

def filtrar_anos_disponiveis(despesas = None):# Uma funcao que extrai apenas os anos das despesas existentes na lista

    if despesas is None:
        despesas = carregar_despesas()

    anos = set()
    for despesa in despesas:
        data = despesa.get("data")# recebe o campo data da lista de despesas
        if not data:
            continue
        ano = int(data.split("-")[0])#aqui ele retira os "-" assim os valores da data se separam entre
        anos.add(ano)                # virgulas e ele recebe apenas o valor na posição 0.

    return list(anos)

def filtrar_mes_selecionado(mes):# funcao onde se pega todas as despesas do mês selecionado
    despesas = carregar_despesas()

    return[
        d for d in despesas
        if d.get("data") and int(d["data"].split("-")[1]) == int(mes)
    ]

def filtrar_meses_disponiveis(despesas = None):

    if despesas is None:
        despesas = carregar_despesas()

    meses = set()
    for despesa in despesas:
        data = despesa.get("data")  # recebe o campo data da lista de despesas
        if not data:
            continue
        mes = int(data.split("-")[1])  # aqui ele retira os "-" assim os valores da data se separam entre
        meses.add(mes)                 # virgulas e ele recebe apenas o valor na posição 1.

    return list(meses)

def filtrar_por_mes_ano(data_mes,data_ano):
    despesas = carregar_despesas()
    lista_mes_ano = []
    for despesa in despesas:

        data = despesa.get("data")
        partes = data.split("-")
        ano = int(partes[0])
        mes = int(partes[1])

        if data_mes == mes and data_ano == ano:
            lista_mes_ano.append(despesa)

    return lista_mes_ano
