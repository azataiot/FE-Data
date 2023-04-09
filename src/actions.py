from pathlib import Path
import pandas as pd


# read the csv file into a dataframe

def add(symbol: str, output_path: Path | str):
    df = pd.read_csv(output_path)
    df_to_add = pd.read_csv(actions_folder / "add.csv", comment="#")
    df = df.append(df_to_add, ignore_index=True)
    df.to_csv(output_path, index=False)
    print(f"Added {symbol} to {output_path}")


if __name__ == "__main__":
    cwd = Path.cwd()
    actions_folder = cwd / "../actions"
    df_to_add = pd.read_csv(actions_folder / "add.csv", comment="#")
