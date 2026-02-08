from core.despesas_validacoes_core import *
from core.despesas_arquivo_core import *

def adicionar_despesa_core(valor,descricao,categoria,data):
    despesas = carregar_despesas()

    if despesas:
        ultimo_id = despesas [-1]["id"]
        novo_id = ultimo_id +1
    else:
        novo_id = 1

    despesa = {
        "id": novo_id,
        "valor": validar_valor(valor),
        "descricao": validar_descricao(descricao),
        "categoria": validar_categoria(categoria),
        "data": validar_data(data)
    }
    despesas.append(despesa)
    salva_despesas(despesas)
