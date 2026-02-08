
# 💰 Gerenciador de Despesas Pessoais (Python/Tkinter)

## 🔹 Descrição

Aplicativo de gerenciamento de despesas pessoais desenvolvido em Python com interface gráfica em Tkinter.
Permite adicionar, listar, filtrar e deletar despesas de forma segura e intuitiva, mantendo uma arquitetura limpa GUI + CORE.

## 🔹 Funcionalidades

## 📝 Adicionar Despesa

Insere valor, descrição, categoria e data.

IDs gerados automaticamente no CORE.

## 📊 Listar Despesas

 - Tabela organizada com todas as despesas.

 - Coluna ID usada internamente para DELETE.

## 🔍 Filtrar Despesas

 - Por categoria ou período.

 - Resultados exibidos na mesma tela, mantendo contexto.

## ❌ Excluir Despesa (DELETE)

 - Seleção direta da linha na tabela.

 - Confirmação antes de apagar, evitando erros.

## ✅ Validação de Dados

 - Valores, descrições, categorias e datas validados no CORE.

## 🏗 Arquitetura Limpa

 - Lógica de dados isolada no CORE.

 - GUI apenas exibe dados e recebe inputs do usuário.

## 🔹 Tecnologias

 - Python 3.13

 - kinter (GUI)

 - SON (armazenamento de dados)

## 🔹 Estrutura do Projeto
```
gerenciador_despesas/
├── gui/
│   ├── telas/
│   │   ├── tela_adicionar.py
│   │   ├── tela_listar.py
│   │   └── ...
│   └── app.py
├── core/
│   ├── despesas_arquivo_core.py
│   ├── despesas_validacoes_core.py
│   └── ...
├── data/
│   └── despesas.json
└── README.md
```

## 🔹 Como Rodar

1- Clone o repositório:
```bash
git clone <URL_DO_REPOSITORIO>
```
2- Entre na Pasta do Projeto
```bash
cd gerenciador_despesas
```
3- Execute a aplicação:
```bash
python gui/main.py
```

## 🔹 Próximos Passos (Planejados)

 - 📈 Estatísticas avançadas com gráficos.

 - 📂 Exportação de despesas para CSV.

 - 🎨 Melhorias na UX (tema visual, cores, ícones).


