import pandas as pd
import numpy as np
import pyarrow as pa
import scipy.stats as stats
from .data import Find_N_datasets
from matplotlib.ticker import FuncFormatter

from sklearn import svm

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

paths = Find_N_datasets(N_files=2, path_loc='raw')
motor = pd.read_csv(paths[0], sep=";")
claims = pd.read_csv(paths[1], sep=";")

def not_average_feature(df: pd.DataFrame, old_name: list[str], new_name: list[str]):
    # Curating useful classification columns
    df[new_name[0]] = (
        df[old_name[0]] <
        (df[old_name[0]].median() - df[old_name[0]].std())
    ).astype(int)

    df[new_name[1]] = (
            df[old_name[1]] >
            (df[old_name[1]].median() + df[old_name[1]].std())
        ).astype(int)
    

def OHE_imputation_frame(df: pd.DataFrame,
                        cols: list[str],
                        msg: bool = True, 
                        to_rename: dict = {"Type_risk_1":"Is_Motorbike",
                                            "Type_risk_2":"Is_Van",
                                            "Type_risk_3":"Is_Passenger_Car",
                                            "Type_risk_4":"Is_Agricultural",
                                            "Type_fuel_0.0":"Fuel_Petrol",
                                            "Type_fuel_1.0":"Fuel_Diesel",
                                            "Type_fuel_missing":"Fuel_Unknown"}):
    temp = []
    acceptance = 0.05 # We only accept p values less than this

    for col in cols:
        if msg: print(f"\n{col}\n")
        table = pd.crosstab(
            df['Length_missing'],
            df[col]
        )
        if msg: print(f"{table}\n")
        chi2, p, dof, ex = stats.chi2_contingency(table,)
        if msg: print(f"p-value: {p}") 
        if p <= acceptance: # type: ignore
            temp.append(col)

    print(temp)
    temp_2 = temp.copy()
    for item in temp_2:
        if len(df[item].unique()) == 2:
            temp.remove(item)
    if msg: print(temp)

    encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")

    encoded = encoder.fit_transform(df[temp])

    encoded_df = pd.DataFrame(
        encoded,
        columns=encoder.get_feature_names_out(temp),
        index=df.index
    )

    df = pd.concat([df, encoded_df], axis=1)
    df.drop(columns=temp, inplace=True)
    df.rename(columns=to_rename,inplace=True)

