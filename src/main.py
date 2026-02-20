from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

from limpeza import limpar_dados
from analise import (
    resumo_geral,
    faturamento_por_cliente,
    faturamento_por_mes,
    faturamento_por_categoria,
)

PASTA_DATA = Path("data")
PASTA_OUTPUT = Path("output")


def ler_multiplos_csv(pasta: Path) -> pd.DataFrame:
    arquivos = sorted(pasta.glob("*.csv"))

    if not arquivos:
        raise FileNotFoundError(
            f"Nenhum arquivo CSV encontrado em: {pasta.resolve()}"
        )

    dfs = []

    for arq in arquivos:
        print(f"Lendo arquivo: {arq.name}")
        df = pd.read_csv(arq)
        df["arquivo_origem"] = arq.name
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)


def salvar_grafico_faturamento_mes(df_mes: pd.DataFrame, caminho: Path) -> None:
    plt.figure()
    plt.plot(df_mes["mes"], df_mes["valor"], marker="o")
    plt.xticks(rotation=45, ha="right")
    plt.title("Faturamento por mês")
    plt.xlabel("Mês")
    plt.ylabel("Faturamento")
    plt.tight_layout()
    plt.savefig(caminho, dpi=150)
    plt.close()


def main():
    print("Iniciando Projeto 3...")

    PASTA_OUTPUT.mkdir(exist_ok=True)

    # 1) Leitura
    df_raw = ler_multiplos_csv(PASTA_DATA)

    # 2) Limpeza
    df = limpar_dados(df_raw)

    base_csv = PASTA_OUTPUT / "base_tratada.csv"
    df.to_csv(base_csv, index=False, encoding="utf-8")

    # 3) Análises
    df_resumo = resumo_geral(df)
    df_top_clientes = faturamento_por_cliente(df, top_n=10)
    df_mes = faturamento_por_mes(df)
    df_cat = faturamento_por_categoria(df)

    # 4) Relatório Excel
    relatorio_xlsx = PASTA_OUTPUT / "relatorio_final.xlsx"

    with pd.ExcelWriter(relatorio_xlsx, engine="openpyxl") as writer:
        df_resumo.to_excel(writer, index=False, sheet_name="Resumo")
        df_top_clientes.to_excel(writer, index=False, sheet_name="Top_Clientes")
        df_mes.to_excel(writer, index=False, sheet_name="Por_Mes")
        df_cat.to_excel(writer, index=False, sheet_name="Por_Categoria")
        df.to_excel(writer, index=False, sheet_name="Base_Limpa")

    # 5) Gráfico
    grafico_png = PASTA_OUTPUT / "grafico_faturamento_mes.png"
    salvar_grafico_faturamento_mes(df_mes, grafico_png)

    print("Projeto finalizado com sucesso!")
    print(f"Relatório salvo em: {relatorio_xlsx}")
    print(f"Gráfico salvo em: {grafico_png}")

    grafico_cat_png = PASTA_OUTPUT / "grafico_faturamento_categoria.png"
    salvar_grafico_faturamento_categoria(df_cat, grafico_cat_png)

    print(f"📄 Base tratada: {base_csv}")
    print(f"📈 Gráfico categoria: {grafico_cat_png}")


if __name__ == "__main__":
    main()

def salvar_grafico_faturamento_categoria(df_cat: pd.DataFrame, caminho: Path) -> None:
    if df_cat.empty:
        return

    plt.figure()
    plt.bar(df_cat["categoria"], df_cat["valor"])
    plt.xticks(rotation=45, ha="right")
    plt.title("Faturamento por categoria")
    plt.xlabel("Categoria")
    plt.ylabel("Faturamento")
    plt.tight_layout()
    plt.savefig(caminho, dpi=150)
    plt.close()