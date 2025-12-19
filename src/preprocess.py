import pandas as pd

def load_covid_data(path: str) -> pd.DataFrame:
   
    df = pd.read_csv(path)
    return df

def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    
    cols_needed = [
        "location",
        "date",
        "total_deaths",
        "total_deaths_per_million",
        "people_vaccinated",
        "median_age",
        "aged_65_older"
    ]

    available_cols = [c for c in cols_needed if c in df.columns]
    df = df[available_cols]

    return df
