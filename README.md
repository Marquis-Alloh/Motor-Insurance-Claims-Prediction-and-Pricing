# Motor Insurance: Claims Prediction and Pricing

## Overview

The main goal of this project is to answer questions an insurer may want to know from their customer data. While teaching me the skills required to hit the ground running in spaces that require an understanding of the following:

### Technical Skills and Knowledge

- Mathematics, Probability and Statistics

- Machine Learning and Modeling Fundamentals

- CI Engineering, Data Structures and Algorithms

- Data Visualisation, Wrangling and Analysis

- Database Management, Storage Optimization

- Cloud Computing (AWS)

### Questions of Interest

In addition, this project seeks to answer the following questions:

- How to clean a dataset when simple removal of data would significantly impact accuracy?

- How to create code that is scalable both operationally and in modelling?

- What are the general trends found in the data?

- How to perform quality assurance checks responsibly and effectively?

- Who claims?
    - What are the demographics?

- How much do they cost?

- What variables drive risk?

- What should the insurer charge?

### Dataset

The dataset being used is a [dataset of an actual motor vehicle insurance portfolio](https://data.mendeley.com/datasets/compare/5cxyb5fp4f?utm_source=chatgpt.com) for an insurer.

The data is formatted as a spreadsheet, encompassing the primary activities over a span of three full years (November 2015 to December 2018) concerning non-life motor insurance portfolio. This dataset comprises 105,555 rows and 30 columns. Each row signifies a policy transaction, while each column represents a distinct variable.


## Project Structure

`TBD` means “to be decided” and marks a placeholder for content that will be added later.

## Project Structure

```text
Motor-Insurance-Claims-Prediction-and-Pricing/
├── data/
│   ├── raw/                              # Original data files (local only; not committed)
│   │   ├── Claims.csv                   # Claims data
│   │   ├── Motor.csv                    # Motor policy data
│   │   └── Descriptive.xlsx             # Data dictionary
│   ├── processed/                        # Cleaned and transformed datasets
│   │   └── TBD.csv
│   └── README.md                         # Data sources, licensing and setup
├── notebooks/
│   ├── TBD.ipynb                         
│   ├── Descriptive.sql                        # Descriptive analysis
├── sql/
│   ├── schema.sql                        # Database tables and constraints
│   ├── load_data.sql                     # Data loading and transformation queries
│   └── analysis_queries.sql              # Reusable analytical queries
├── src/
│   └── insurance_pricing/
│       ├── __init__.py
│       ├── data.py                       # Data loading and inspection
│       ├── cleaning.py                   # Data cleaning and validation
│       ├── features.py                   # Feature engineering
│       ├── modelling.py                  # Frequency and severity models
│       ├── evaluation.py                 # Model diagnostics and comparisons
│       └── pricing.py                    # Pure premium calculations
├── tests/
│   ├── test_data.py
│   ├── test_features.py
│   ├── test_modelling.py
│   ├── test_pricing.py
│   └── test_database.py
├── api/
│   └── main.py                           # Prediction API endpoint
├── reports/
│   ├── figures/                          # Generated plots and visualisations
│   └── model_comparison.md               # Model evaluation findings
├── .github/
│   └── workflows/
│       └── tests.yml                     # Automated tests using GitHub Actions
├── .env.example                          # Example environment configuration
├── .gitignore                            # Files excluded from Git
├── pyproject.toml                        # Project metadata, dependencies and tooling
└── README.md                             # Project overview and setup instructions
```
