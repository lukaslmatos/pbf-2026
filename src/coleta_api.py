from pathlib import Path 
import requests

# TODO: Coloque aqui a URL exata da API pública que você consultou
URL_API = "https://dados.gov.br/dados/conjuntos-dados/bolsa-familia---beneficios-basicos-e-variaveis"

CAMINHO_RAW = Path("data/raw/bolsa_familia_api.csv")


def coletar_dados_api(url: str = URL_API, destino: Path = CAMINHO_RAW) -> Path:
    """Consulta a API de dados públicos e salva o arquivo bruto em CSV."""
    destino.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        destino.write_bytes(response.content)
        print(f"Dados coletados da API com sucesso em: {destino}")
    except requests.RequestException as erro:
        print(f"Aviso: não foi possível consultar a API no momento ({erro}).")
        if destino.exists():
            print(f"Usando o arquivo bruto já salvo localmente em: {destino}")
        else:
            raise FileNotFoundError(
                "Arquivo bruto não encontrado em data/raw/bolsa_familia_api.csv."
            )
    return destino


if __name__ == "__main__":
    coletar_dados_api()
