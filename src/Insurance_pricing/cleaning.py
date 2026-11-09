import pandas as pd
from configparser import ConfigParser
from .data import Find_N_datasets, inspect_dataset

def clean_dates(df):
    """
    Formats the dates correctly

    df: dataframe
    """
    df = df.copy()

    for col in df.columns:
        if "date" in col.lower():
            df[col] = pd.to_datetime(
                df[col],
                dayfirst=True,
                errors="coerce" # Converts the invalid values into NaT for dates or NaN for numeric values
            )
        elif "year" in col.lower():
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )
    return df




def clean_names(df: pd.DataFrame, col_names: dict, lower: bool = False):
    if col_names is not None:
        reject = []
        for i in col_names.keys():
            if i not in df.columns:
                reject.append(i)
                col_names.pop(i)
        if lower: df.rename(str.lower, axis='columns', columns=col_names, inplace=True)
        else: df.rename(columns=col_names, inplace=True)
        if len(reject)>0: print(f"the rejected columns {reject}")
        
def clean_types(df):
    """
    Formats the types in the datasets
    
    df: dataframe
    """
    df["Type_fuel"] = df["Type_fuel"].map({
            "D": 0,
            "P": 1
        })
    return df
