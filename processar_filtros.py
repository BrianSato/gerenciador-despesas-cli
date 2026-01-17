import despesas_menu as desp_menu
import resultados_filtros as res_filt
import despesas_adicionar
from despesas_mensagens import ERROS
from despesas_menu import msg_data_inicio, msg_data_fim

def processar_filtros(despesas):

    desp_menu.menu_filtros()
    opcao_filtros = despesas_adicionar.ler_opcao()

    if opcao_filtros == 1:
        res_filt.res_filtrar_categoria(despesas)
    elif opcao_filtros == 2:
        msg_data_inicio()
        data_inicio = despesas_adicionar.obter_data()
        msg_data_fim()
        data_fim  =  despesas_adicionar.obter_data()
        res_filt.res_filtrar_data(despesas, data_inicio,data_fim)
    elif opcao_filtros == 0:
        return
    else:
        print(ERROS["erro_valor"])

