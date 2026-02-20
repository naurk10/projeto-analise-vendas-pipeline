import pandas as pd

def resumo_geral(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "metricas": [
            "linhas",
            "clientes_unicos",
            "produtos_unicos",
            "faturamento_total",
            "ticket_medio",
        ],
        "valor": [
            len(df),
            df["cliente"].nunique(),
            df["produto"].nunique(),
            df["valor"].sum(),
            df["valor"].mean(),
        ],
    })

def faturamento_por_cliente(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    return (
        df.groupby("cliente", as_index=False)["valor"].sum()
        .sort_values("valor", ascending=False)
        .head(top_n)
    )

def faturamento_por_mes(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("mes", as_index=False)["valor"].sum()
        .sort_values("mes")
    )

def faturamento_por_categoria(df: pd.DataFrame) -> pd.DataFrame:
    if "categoria" not in df.columns:
        return pd.DataFrame(columns=["categoria", "valor"])
    return (
        df.groupby("categoria", as_index=False)["valor"].sum()
        .sort_values("valor", ascending=False)
    )