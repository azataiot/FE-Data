from pathlib import Path
from pandas import DataFrame


def check_file_exists(file_path):
    """Check if a file exists at the given path.

    Args:
        file_path (str): The path to the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return Path(file_path).is_file()


def get_file_list(dir_path, file_ext):
    """Get a list of files in a directory with a given file extension.

    Args:
        dir_path (str): The path to the directory.
        file_ext (str): The file extension.

    Returns:
        list: A list of files in the directory with the given file extension.
    """
    return [f for f in Path(dir_path).glob(f"*.{file_ext}")]


def extract_columns(
    df: DataFrame, column_names: list[str] | tuple[str] | set[str]
) -> DataFrame:
    """Extract columns from a dataframe.

    Args:
        df (DataFrame): The dataframe to extract columns from.
        column_names (list): A list of column names to extract.

    Returns:
        DataFrame: A dataframe with only the extracted columns.
    """
    return df[column_names]
