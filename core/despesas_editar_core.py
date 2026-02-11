from core.despesas_arquivo_core import *
from core.despesas_validacoes_core import validar_valor, validar_descricao, validar_categoria, validar_data


def editar_despesa_core(id_despesa,valor, descricao, categoria, data):
    # carrega a lista de despesas
    despesas = carregar_despesas()

    # cria uma nova lista sem a  despesa que tem o ID
    for despesa in despesas:
        if despesa["ID"] == id_despesa:

            despesa["valor"] = validar_valor(valor)
            despesa["descricao"] = validar_descricao(descricao)
            despesa["categoria"] = validar_categoria(categoria)
            despesa["data"] = validar_data(data)

            break
    else:
        return False

    # salva a lista atualizada
    salva_despesas(despesas)
    return True