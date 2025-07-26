from pathlib import Path
import pandas as pd

# Diretório dos CSVs (relativo ao projeto)
CSV_DIR = Path(__file__).resolve().parents[2] / "data" / "csv_files"


def load_csv_data():
    """Carrega todos os arquivos CSV do diretório CSV_DIR.

    Retorna um único DataFrame se houver apenas um CSV ou uma lista de DataFrames
    se houver múltiplos arquivos.
    """
    dataframes = []
    for csv_file in CSV_DIR.glob("*.csv"):
        df = pd.read_csv(csv_file)
        dataframes.append(df)

    if not dataframes:
        raise FileNotFoundError(f"Nenhum CSV encontrado em {CSV_DIR}")

    return dataframes[0] if len(dataframes) == 1 else dataframes
