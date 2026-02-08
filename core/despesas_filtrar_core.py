from datetime import datetime
from core.despesas_arquivo_core import carregar_despesas

despesas = carregar_despesas()

def filtrar_por_categoria(categoria):

     return[
        despesa for despesa in despesas
        if despesa.get("categoria") == categoria
    ]

def filtrar_por_periodo(data_inicio, data_fim):

    data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date()
    data_fim = datetime.strptime(data_fim,"%Y-%m-%d").date()

    resultado = []
    for despesa in despesas:
        if "data" in despesa:
            data_despesa = datetime.strptime(despesa["data"],"%Y-%m-%d").date()
            if data_inicio <= data_despesa <= data_fim:
                resultado.append(despesa)
    return resultado

def filtrar_anos_disponiveis():  # Uma funcao que extrai apenas os anos das despesas existentes na lista
    anos = set()

    for despesa in despesas:
        data = despesa.get("data")# recebe o campo data da lista de despesas
        if not data:
            continue
        ano = int(data.split("-")[0])# <- aqui ele retira os "-" assim os valores da data se separam entre virgulas e ele recebe apenas o valor na posição 0.
        anos.add(ano)

    return list(anos)

def filtrar_por_mes_ano(data_mes,data_ano):
    lista_mes_ano = []
    for despesa in despesas:

        data = despesa.get("data")
        partes = data.split("-")
        ano = int(partes[0])
        mes = int(partes[1])

        if data_mes == mes and data_ano == ano:
            lista_mes_ano.append(despesa)

    return lista_mes_ano
