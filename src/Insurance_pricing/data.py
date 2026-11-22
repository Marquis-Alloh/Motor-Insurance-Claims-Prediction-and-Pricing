import pandas as pd
import matplotlib.pyplot as plt
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

def Dates_to_times(
    dates_of_interest: list[pd.Series],
    duration: bool = False
) -> pd.Series | list[pd.Series]:

    Today = pd.Timestamp.today().normalize()
    Year_const = 365.25

    dates = [
        pd.to_datetime(item, errors="coerce")
        for item in dates_of_interest
    ]

    if not duration:
        temp = [
            (Today - item).dt.days / Year_const
            for item in dates
        ]

    else:
        if len(dates) % 2 != 0:
            raise ValueError(
                "Dates provided must be in pairs when calculating durations."
            )

        temp = []

        for start, end in zip(dates[::2], dates[1::2]):
            temp.append(
                (end - start).dt.days / Year_const
            )

    if len(temp) == 1:
        return temp[0]

    return temp

def plot_df(df, x_col, y_col, kind="scatter", title=None, figsize=(8, 5)):

    # Check that columns exist
    if x_col not in df.columns or y_col not in df.columns:
        raise ValueError("Specified columns must exist in the DataFrame.")

    # Remove rows with missing x or y values
    data = df[[x_col, y_col]].dropna()

    # Create figure
    fig, ax = plt.subplots(figsize=figsize)

    # Plot data
    if kind == "scatter":
        ax.scatter(data[x_col], data[y_col])
    elif kind == "line":
        ax.plot(data[x_col], data[y_col], marker="o")
    else:
        raise ValueError("kind must be either 'scatter' or 'line'.")

    # Labels and formatting
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(title if title else f"{y_col} against {x_col}")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    return fig, ax
    

def missing_length_by_age(df, age_col, n_bins, condition=None):

    # Apply condition if one is provided
    if condition is not None:
        df = df.loc[condition].copy()

    # Remove records without an age value
    df = df.loc[df[age_col].notna()].copy()

    # Divide age into N intervals
    df['Age_bin'] = pd.cut(df[age_col], bins=n_bins)

    # Count missing Length values and total observations
    results = (
        df.groupby('Age_bin', observed=False)['Length_missing']
        .agg(['sum', 'count'])
    )

    # Store results in lists
    age_midpoints = [interval.mid for interval in results.index]
    missing_counts = results['sum'].tolist()
    total_counts = results['count'].tolist()

    # Calculate percentage missing in each age interval
    missing_percentages = (
        results['sum'] / results['count'].replace(0, np.nan) * 100
    ).tolist()

    return age_midpoints, missing_counts, total_counts, missing_percentages

def LD_missingness_acceptability():
    """
    Function assesses if the Lapse date missingness is expected/purposful by
    returning records of the counts, percentages and verdict (True or False)
    for each combination of claims and missing lapse dates
    """
    paths = Find_N_datasets(N_files=2, path_loc='raw')
    motor = pd.read_csv(paths[0], sep=";")
    claims = pd.read_csv(paths[1], sep=";")

    # Create a copy of the motor dataset
    motor_check = motor.copy()

    # Get the IDs present in the claims dataset
    claim_ids = claims["ID"].dropna().astype("string").str.strip()

    # Check whether each motor ID appears in the claims dataset
    motor_ids = motor_check["ID"].astype("string").str.strip()
    motor_check["Claim_Made"] = motor_ids.isin(claim_ids)

    # Create Date_lapse status
    motor_check["Date_lapse_Status"] = np.where(
        motor_check["Date_lapse"].isna(),
        "Missing",
        "Recorded"
    )

    # Count records for each combination
    counts = pd.crosstab(
        motor_check["Claim_Made"],
        motor_check["Date_lapse_Status"]
    )

    # Calculate percentages within each claim group
    percentages = (
        counts.div(counts.sum(axis=1), axis=0) * 100
    )

    return counts, percentages.round(2), bool(round(percentages.round(2)["Missing"][False], 2) >= round(percentages.round(2)["Missing"][True],2) + 5)
