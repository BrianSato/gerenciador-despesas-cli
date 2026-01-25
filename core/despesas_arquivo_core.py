from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR/"data"
ARQUIVO_JSON = DATA_DIR/"despesas.json"

#  FUNCOES PARA SALVAR  E CARREGAR OS DADOS EM ARQUIVO

def salva_despesas(despesas):
    DATA_DIR.mkdir(exist_ok=True)

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
