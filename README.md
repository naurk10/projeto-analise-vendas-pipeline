# 📊 Projeto 3 — Pipeline Profissional de Análise de Vendas

Este projeto implementa um pipeline completo de análise de dados utilizando Python e Pandas, com execução via terminal.

O objetivo é simular um cenário real de análise de vendas com múltiplos arquivos CSV, limpeza automatizada, geração de relatórios e criação de gráficos.

---

## 🚀 Funcionalidades

✔ Leitura automática de múltiplos arquivos CSV  
✔ Padronização e limpeza de dados  
✔ Consolidação de base tratada  
✔ Geração de relatório Excel com múltiplas abas  
✔ Criação de gráficos automáticos  
✔ Execução via terminal  
✔ Estrutura organizada por módulos  

---

## 📂 Estrutura do Projeto

projetos_3_analise_completa/
│
├── data/ # Arquivos CSV de entrada
├── output/ # Arquivos gerados automaticamente
│ ├── base_tratada.csv
│ ├── grafico_faturamento_mes.png
│ └── grafico_faturamento_categoria.png
│
├── src/
│ ├── main.py # Script principal
│ ├── limpeza.py # Funções de limpeza
│ └── analise.py # Funções de análise
│
├── requirements.txt
└── README.md

## 🛠 Tecnologias Utilizadas

- Python
- Pandas
- Matplotlib
- OpenPyXL
- Git / GitHub

---

## ▶ Como Executar o Projeto

### 1️⃣ Criar ambiente virtual

```bash
python -m venv .venv

```
2️⃣ Ativar ambiente virtual (Windows PowerShell)

```bash
.\.venv\Scripts\Activate.ps1

```
3️⃣ Instalar dependências

```bash
pip install -r requirements.txt

```
4️⃣ Executar o pipeline

```bash
python src/main.py


