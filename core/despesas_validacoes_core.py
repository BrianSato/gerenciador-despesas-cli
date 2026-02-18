from datetime import datetime
from core.despesas_mensagens_core import CATEGORIAS,ERROS

lista_categorias = list(CATEGORIAS.values())

def validar_valor(valor):
    try:
        valor = float(valor)
        if valor <=0:
            raise  ValueError
        return  valor
    except ValueError:
        raise ValueError(ERROS["error_value"])

def validar_descricao(descricao):
    descricao = descricao.strip()
    if not descricao:
         raise ValueError(ERROS["error_description"])
    return descricao

def validar_categoria(categoria):
    if categoria not in CATEGORIAS.values():
        raise  ValueError(ERROS["error_category"])
    return categoria

def validar_data(data):
    data = data.strip()

    if not data:
        return  datetime.today().strftime("%Y-%m-%d")

    try:
        datetime.strptime(data,"%Y-%m-%d")
        return data

    except ValueError:
        raise ValueError(ERROS["error_date"])


