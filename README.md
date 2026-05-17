# 🦠 COVID Impact Analysis

[![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter)](https://jupyter.org)
[![Data](https://img.shields.io/badge/Data-Our%20World%20in%20Data-green?style=for-the-badge)](https://ourworldindata.org)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()

> 📊 A data-driven project analyzing COVID-19 death rates, vaccination trends, and key demographic indicators using datasets from Our World in Data (OWID).

---

## 🎯 Project Goal

To explore the factors that influenced COVID-19 mortality across countries, including:
- 🧬 Demographics (age groups, median age)
- 🚬 Smoking rates by region
- 🏥 Healthcare capacity
- 📋 Government response (stringency index)

**Key Questions Explored:**
- 🌍 What was the global COVID-19 death rate as of September 2020?
- 💀 Which countries had the highest death rates among significantly affected nations?
- 🚬 How did smoking rates vary across regions?
- ⚡ Which countries saw the fastest death acceleration in the 30 days after their first recorded death?

---

## 🔑 Key Findings

| # | 🔍 Finding | 📈 Value |
|---|-----------|---------|
| 1 | 🌍 Global COVID-19 death rate | **~4.1%** *(as of Sep 2020)* |
| 2 | 💀 Highest death rate (10,000+ cases) | **Italy at 11.9%** |
| 3 | 🚬 Highest smoking country | **Nauru** *(121.5% combined men + women)* |
| 4 | ⚡ Fastest death acceleration (30 days) | **San Marino** *(766 deaths/million)* |
| 5 | ⚠️ Notable: Yemen | **28.9% death rate** *(small case count)* |

---

## 🗃️ Datasets Used

| 📁 Dataset | 🔗 Source | 📝 Description |
|-----------|----------|---------------|
| `owid-covid-data` | Our World in Data | Global COVID cases, deaths, vaccinations *(41 columns)* |
| `BCG_country_data` | Kaggle BCG Hackathon | Country demographics, smoking rates, income groups *(31 columns)* |
| `death_cases_after_first_death` | Kaggle | Deaths per million tracked from day of first death *(62 columns)* |

---

## 🔬 Analysis Performed

### 1️⃣ Global Death Rate Calculation
```python
global_death_rate = (df['total_deaths'].sum() / df['total_cases'].sum()) * 100
# Result: ~4.1%
```

### 2️⃣ Country-Level Death Rate Ranking
- Filtered countries with **>10,000 cases** to remove statistical noise
- Top 10 worst-affected: Italy, Mexico, UK, Belgium, Ecuador, France, Sweden...

### 3️⃣ Demographic Analysis
- Explored `median_age`, `aged_65_older`, `aged_70_older` distributions
- Global median age across dataset: **31.3 years**

### 4️⃣ Smoking Rate Analysis
- Combined men + women smoker percentages by country
- Identified top smoking nations by region *(Asia-Pacific leads globally)*

### 5️⃣ Death Trajectory Tracking
- Tracked deaths per million at **10-day intervals** after first recorded death
- Identified fastest-escalating countries in first 30 days post first death

### 6️⃣ Reusable Data Pipeline
```python
def load_covid_data(path: str) -> pd.DataFrame:
    """Load OWID COVID dataset from given path"""

def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """Select key columns: location, date, total_deaths, median_age..."""
```

---

## 📁 Project Structure

```
Covid_Impact_analysis/
│
├── 📂 data/
│   └── train_dataset/
│       ├── task_2-owid-covid-data-22_September_2020.csv
│       ├── BCG_country_data.csv
│       └── task_2-COVID-19-death_cases_per_country_after_first_death.csv
│
├── 📓 notebooks/
│   └── analysis.ipynb          ← Main analysis notebook
│
├── 🐍 src/                     ← Reusable Python functions
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 Python 3.13 | Core language |
| 🐼 Pandas | Data loading, cleaning, groupby analysis |
| 📊 Matplotlib | Visualizations |
| 🎨 Seaborn | Statistical plots |
| 🤖 Scikit-learn | ML modeling (upcoming) |

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/joonhubb/Covid_Impact_analysis.git
cd Covid_Impact_analysis

# Install dependencies
pip install -r requirements.txt

# Launch notebook
jupyter notebook notebooks/
```

---

## 🔮 Next Steps

- [ ] 📊 Add visualizations — bar charts, heatmaps, time series
- [ ] 🔗 Correlate smoking & age demographics with death rates
- [ ] 🤖 Build regression model to predict death rates from demographics
- [ ] 💉 Add BCG vaccination coverage analysis

---

## 👨‍💻 Author

**Joon** — IIT Madras BS Data Science Student

---

<div align="center">
⭐ <b>Star this repo if you found it useful!</b> ⭐
</div>

