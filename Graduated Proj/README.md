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


## Project Structure

TBD: to be decided, a placeholder showing it's going to be updated in the future.

motor-insurance-pricing/
├── data/
│   ├── raw/                       # Original dataset; not committed to Git
│   ├──── Claims.csv               # Dataset containing the claims made
│   ├──── Motor.csv                # Dataset containing policies of interest
│   ├──── Descriptive.xlsx         # Data dictionary with descriptions of variables in the datasets
│   ├── processed/                 # Cleaned and transformed datasets
│   ├────TBD.csv
│   └── README.md                  # Data sources, licensing and setup
├── notebooks/
│   ├── TBD.ipynb
├── sql/
│   ├── schema.sql                 # Database tables and constraints
│   ├── load_data.sql              # SQL loading / transformation queries
│   └── analysis_queries.sql       # Reusable analytical queries
├── src/
│   └── insurance_pricing/
│       ├── __init__.py
│       ├── data.py                # Data loading and validation
│       ├── features.py            # Feature engineering
│       ├── modelling.py           # Frequency and severity models
│       ├── evaluation.py          # Model diagnostics and comparisons
│       └── pricing.py             # Pure premium calculations
├── tests/
│   ├── test_data.py
│   ├── test_features.py
│   ├── test_modelling.py
│   ├── test_pricing.py
│   └── test_database.py
├── api/
│   └── main.py                    # FastAPI prediction endpoint
├── reports/
│   ├── figures/
│   └── model_comparison.md
├── .github/
│   └── workflows/
│       └── tests.yml              # Automated testing with GitHub Actions
├── .env.example                   # Example configuration; no real secrets
├── .gitignore
├── pyproject.toml                 # Dependencies and development tools
└── README.md