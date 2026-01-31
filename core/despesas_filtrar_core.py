from datetime import datetime

from core.despesas_validacoes_core import validar_data


def filtrar_por_categoria(despesas, categoria):

     return[
        despesa for despesa in despesas
        if despesa.get("categoria") == categoria
    ]

def filtrar_por_periodo(despesas, data_inicio, data_fim):

    data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date()
    data_fim = datetime.strptime(data_fim,"%Y-%m-%d").date()

    resultado = []
    for despesa in despesas:
        if "data" in despesa:
            data_despesa = datetime.strptime(despesa["data"],"%Y-%m-%d").date()
            if data_inicio <= data_despesa <= data_fim:
                resultado.append(despesa)
    return resultado
