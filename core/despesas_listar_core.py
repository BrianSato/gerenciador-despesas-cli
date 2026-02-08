from core.despesas_arquivo_core import carregar_despesas

def listar_despesas_core():
    despesas = carregar_despesas()
    return despesas
