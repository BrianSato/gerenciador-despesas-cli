from datetime import datetime

def filtrar_por_categoria(despesas, categoria_var):

     return[
        despesa for despesa in despesas
        if despesa.get("categoria") == categoria_var
    ]

def filtrar_por_periodo(despesas, data_inicio, data_fim):

    return[
        despesa for despesa in despesas
        if "data" in despesa and data_inicio <= despesa["data"] <= data_fim
    ]