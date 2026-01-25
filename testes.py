from core.despesas_listar_core import listar_despesas
from core.despesas_arquivo_core import  carregar_despesas

despesas = carregar_despesas()

print("DEBUG:", despesas)
print(listar_despesas(despesas))

