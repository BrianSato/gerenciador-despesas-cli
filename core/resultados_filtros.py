from despesas_filtrar_core import filtrar_por_categoria as catg_filt
from despesas_adicionar_core import validar_categoria as catg_val
from despesas_filtrar_core import  filtrar_por_periodo as perio_filt
from despesas_mensagens_core import ERROS
from cli.comando.despesas_menu import msg_opcao_catg, msg_opcao_perid

def res_filtrar_categoria(despesas):
    categoria = catg_val()
    filtradas = catg_filt(despesas, categoria)
    if not filtradas:
        print(ERROS["erro_categoria"])
    else:
        msg_opcao_catg()
        print(f"---- Categoria : {categoria} ----")
        for i, despesa in enumerate(filtradas, start=1):
            print(
                f"{i}. R$ {despesa['valor']:.2f} - "
                f"{despesa['descricao']}"
            )

def res_filtrar_data(despesas, data_inicio, data_fim):
   filtradas = perio_filt(despesas, data_inicio, data_fim)
   if not filtradas:
       print(ERROS["erro_data"])
   else:
       msg_opcao_perid()
       for i , despesa in enumerate(filtradas, start=1):
           print(f"{i}. Data Inicio: {data_inicio} - "
                 f"Data Fim: {data_fim} - "
                 f"R$ {despesa['valor']:.2f} - "
                 f"{despesa['descricao']}"
                 )
