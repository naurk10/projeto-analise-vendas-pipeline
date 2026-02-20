import pandas as pd

COLUNAS_OBRIGATORIAS = ["data", "cliente", "produto", "valor"]

def padronizar_colunas(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df


def limpar_dados(df: pd.DataFrame) -> pd.DataFrame:
    df = padronizar_colunas(df)

    faltando = [c for c in COLUNAS_OBRIGATORIAS if c not in df.columns]
    if faltando:
        raise ValueError(f"Colunas obrigatórias faltando: {faltando}")

    df = df.copy()

    df["data"] = pd.to_datetime(df["data"], errors="coerce")
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

    df = df.dropna(subset=["data", "cliente", "produto", "valor"])

    df["cliente"] = df["cliente"].astype(str).str.strip()
    df["produto"] = df["produto"].astype(str).str.strip()

    df["mes"] = df["data"].dt.to_period("M").astype(str)

    return df