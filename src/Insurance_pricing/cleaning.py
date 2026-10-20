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

def MCAR_evaluation(df):
    from pyampute.exploration.mcar_statistical_tests import MCARTest # This is the function for the fixing of missing values.
    pass

#new = clean_dates(motor)

# Missing values
#print(motor.isna().sum().sort_values(ascending=False))

# Numerical distributions
#print(motor.describe())

# Repeated rows
#print("Exact duplicate motor rows:", motor.duplicated().sum())