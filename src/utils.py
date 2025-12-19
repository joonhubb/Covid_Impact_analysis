import pandas as pd


def get_top_death_countries(
    df: pd.DataFrame, top_n: int = 10
) -> pd.Series:
    """
    Returns top N countries by maximum COVID deaths per million
    """
    return (
        df.groupby("location")["total_deaths_per_million"]
        .max()
        .sort_values(ascending=False)
        .head(top_n)
    )


def age_death_correlation(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns correlation between age-related indicators and death rate
    """
    age_df = df[
        ["total_deaths_per_million", "median_age", "aged_65_older"]
    ].dropna()

    return age_df.corr()
