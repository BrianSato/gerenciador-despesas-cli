from core.despesas_arquivo_core import *

def deletar_despesa_core(id_para_deletar):
    #carrega a lista de despesas
    despesas = carregar_despesas()

    #cria uma nova lista sema  despesa que tem o ID
    novas_despesas = [d for d in despesas if d["ID"] != id_para_deletar]

    #Se nenhuma despesa foi removida, nenhum ID foi encontrado
    if len(novas_despesas) == len(despesas):
        return False

    #salva a lista atualizada
    salva_despesas(novas_despesas)
    return True
