# COVID Impact Analysis 📊

A data-driven project analyzing COVID-19 death rates, vaccination trends, and key demographic indicators using datasets from Our World in Data (OWID).

**Project Goal** 🎯
To explore the factors that influenced COVID-19 mortality across countries, including demographics, smoking rates, age distribution, and government response (stringency index).
Key Questions Explored:

What was the global COVID-19 death rate as of September 2020?
Which countries had the highest death rates among significantly affected nations?
How did smoking rates vary across regions?
Which countries saw the fastest death acceleration in the 30 days after their first recorded death?


 **Key Findings** 🔍
FindingValue🌍 Global COVID-19 death rate~4.1% (as of Sep 2020)💀 Highest death rate (10,000+ cases)Italy at 11.9%🚬 Highest smoking countryNauru (121.5% combined men + women)⚡ Fastest death acceleration (30 days)San Marino (766 deaths/million)🇮🇳 Notable: Yemen28.9% death rate (small case count)

📊 Datasets Used
DatasetSourceDescriptionowid-covid-dataOur World in DataGlobal COVID cases, deaths, vaccinations (41 columns)BCG_country_dataKaggle BCG HackathonCountry demographics, smoking rates, income groups (31 columns)death_cases_after_first_deathKaggleDeaths per million tracked from day of first death (62 columns)

## Data Source

- [Our World in Data - COVID-19 Dataset](https://www.kaggle.com/datasets/bcgvaccine/hackathon)

**Analysis Performed** 🔬

1. Global Death Rate Calculation
pythonglobal_death_rate = (df['total_deaths'].sum() / df['total_cases'].sum()) * 100
# Result: ~4.1%
2. Country-Level Death Rate Ranking

Filtered countries with >10,000 cases to remove statistical noise
Top 10 worst-affected: Italy, Mexico, UK, Belgium, Ecuador, France, Sweden...

3. Demographic Analysis

Explored median age, aged_65_older, aged_70_older distributions
Global median age across dataset: 31.3 years

4. Smoking Rate Analysis

Combined men + women smoker percentages by country
Identified top smoking nations by region (Asia-Pacific leads)

5. Death Trajectory Tracking

Tracked deaths per million at 10-day intervals after first recorded death
Identified fastest-escalating countries in first 30 days

6. Reusable Data Pipeline
pythondef load_covid_data(path): ...      # Loads OWID dataset
def basic_cleaning(df): ...         # Selects key columns for analysis
