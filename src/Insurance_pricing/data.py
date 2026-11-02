import pandas as pd
import numpy as np
from configparser import ConfigParser
from pathlib import Path

def inspect_dataset(df):
    """
    Performs useful inspection of datasets to provide an overview of dataset qualities

    df: dataframe for inspection
    """
    print(f'''\nInfo of the dataset:\n{df.info()}\n
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ''')

    print(f'''\nChecking the missing values:\n{df.isnull().sum()}\n
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        ''')
    print(f'''Stats for categorical columns:\n\n{df.describe(include=[object])}\n
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ''')
    print(f'''Stats for numerical columns:\n\n{df.describe(include=[np.number])}\n
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ''')

    print(f'''Datatypes in the column:\n\n{df.dtypes}\n
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ''')

    print(f'''First 5 rows of data from dataset:\n\n{df.head()}\n
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ''')


def Find_N_datasets(N_files: int, path_loc: str) -> list[Path]:
    """
    Return N dataset paths from config.ini.
    
    N_files: number of file paths of interest
    path_loc: gives the folder of the paths of interest
    """

    config_file = Path("config.ini").resolve()

    config = ConfigParser()
    if not config.read(config_file):
        raise FileNotFoundError(f"Could not read {config_file}")

    section = f"paths.{path_loc.lower()}"

    if section not in config:
        raise KeyError(f"Missing section: {section}")

    paths = list(config.items(section))[:N_files]

    selected_paths = [
        config_file.parent / file_path
        for name, file_path in paths
    ]

    for (name, _), path in zip(paths, selected_paths):
        print(f"{name}: {path}")

    return selected_paths
