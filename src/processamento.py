from pathlib import Path
import pandas as pd

CAMINHO_RAW = Path("data/raw/bolsa_familia_api.csv")
CAMINHO_PROCESSADO = Path("data/processed/bolsa_familia_processado.csv")


def limpar_e_transformar(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica limpeza básica, padronização de tipos e criação de colunas derivadas."""
    df = df.copy()

    # 1. Padroniza nomes das colunas
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # 2. Remove linhas totalmente vazias e duplicatas
    df = df.dropna(how="all").drop_duplicates()

    # 3. Converte coluna 'ano' para inteiro, se existir
    if "ano" in df.columns:
        df["ano"] = pd.to_numeric(df["ano"], errors="coerce")
        df = df.dropna(subset=["ano"])
        df["ano"] = df["ano"].astype(int)

    # 4. Converte colunas monetárias/numéricas comuns do formato pt-BR para float
    colunas_numericas = ["valor_repassado", "valor", "familias", "beneficio_medio"]
    for col in colunas_numericas:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace("R$", "", regex=False)
                .str.replace(".", "", regex=False)
                .str.replace(",", ".", regex=False)
                .str.strip()
            )
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # 5. Cria coluna derivada de variação percentual anual, se houver ano e valor_repassado
    if "ano" in df.columns and "valor_repassado" in df.columns:
        df = df.sort_values("ano")
        df["variacao_pct_anual"] = df["valor_repassado"].pct_change() * 100

    return df


def main() -> None:
    if not CAMINHO_RAW.exists():
        raise FileNotFoundError(f"Arquivo bruto não encontrado: {CAMINHO_RAW}")

    df_raw = pd.read_csv(CAMINHO_RAW)
    df_processado = limpar_e_transformar(df_raw)

    CAMINHO_PROCESSADO.parent.mkdir(parents=True, exist_ok=True)
    df_processado.to_csv(CAMINHO_PROCESSADO, index=False, encoding="utf-8")
    print(f"Arquivo processado salvo em: {CAMINHO_PROCESSADO}")


if __name__ == "__main__":
    main()
