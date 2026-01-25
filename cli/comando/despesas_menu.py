from core.despesas_mensagens_core import MENSAGENS

def menu():
    print("\n-------GERENCIADOR DE DESPESAS-------")
    print(" 1 - Adicionar despesa:")
    print(" 2 - Listar despesas:")
    print(" 3 - Filtrar despesas por Tipo:")
    print(" 4 - Ver estatisticas:")
    print(" 0 - Sair")

def menu_filtros():
    print("\n------- OPÇÕES DE FILTROS: ---------")
    print("1- Filtrar por categoria:")
    print("2 - Filtrar por periodo:")
    print("0 - Voltar")

def msg_data_inicio():
    print(MENSAGENS["data_inicial"])
def msg_data_fim():
    print(MENSAGENS["data_final"])
def msg_opcao_catg():
    print(MENSAGENS[ "filtro_categora"])
def msg_opcao_perid():
    print(MENSAGENS["filtro_data"])





