import os.path
from pathlib import Path
import json
from utils.caminhos import caminho_base

#PASTA FIXA DO USUÁRIO
PASTA_APP = Path(os.path.expanduser("~"))/ "GerenciadorDespesas"
PASTA_APP.mkdir(exist_ok=True)

ARQUIVO_JSON =  PASTA_APP / "despesas.json"

#FUNCOES PARA GARANTIR ABERTURA DE ARQUIVO JSON TANTO PARA EXE QUANTO PARA PYCHARM
def garantir_arquivo_json():
    base = caminho_base()
    pasta = os.path.join(base,"data")
    arquivo = os.path.join(pasta,"despesas.json")

    #Cria pasta se não existir
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    #Cria arquivo vazio se não existir
    if not os.path.exists(arquivo):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump([],f,indent=4)

    return arquivo

#  FUNCOES PARA SALVAR  E CARREGAR OS DADOS EM ARQUIVO

def salva_despesas(despesas):

    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(despesas,arquivo,ensure_ascii=False, indent=4)

def carregar_despesas():
    if not ARQUIVO_JSON.exists():
        return[]

    with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return[]

