from core.despesas_validacoes_core import (
validar_valor,
validar_descricao,
categoria_var,
validar_data
)

def adicionar_despesa_core(despesas,valor,descricao,categoria,data):

    despesa = {
        "valor": validar_valor(valor),
        "descricao": validar_descricao(descricao),
        "categoria": categoria_var(categoria),
        "data": validar_data(data)
    }
    despesas.append(despesa)
