#IMPORTANDO FUNCOES
import despesas_menu as desp_menu
from core.despesas_mensagens_core import MENSAGENS
from core import despesas_listar_core as desp_list, despesas_adicionar_core, despesas_estatisticas_core as desp_calc, \
    processar_filtros as pf, despesas_arquivo_core as desp_arq
from core.despesas_adicionar_core import adiciona_despesa as desp_add

#CARREGANDO DO ARQUIVO
despesas = desp_arq.carregar_despesas()

# INICIO DO PROGRAMA
while True:
    desp_menu.menu()
    opcao_menu = despesas_adicionar.ler_opcao()

    if opcao_menu == 1:
        desp_add(despesas)
    elif opcao_menu == 2:
        desp_list.listar_despesas(despesas)
    elif opcao_menu == 3:
        pf.processar_filtros(despesas)
    elif opcao_menu == 4:
        desp_calc.mostrar_total_e_media(despesas)
        desp_calc.maior_menor_valor(despesas)
    elif opcao_menu == 0:
        print(MENSAGENS["fim_programa"])
        break
    else:
        print(MENSAGENS["opcao_invalida"])

desp_arq.salva_despesas(despesas)
print(MENSAGENS["despesa_salva"])