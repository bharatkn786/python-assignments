# Week 2 Challenge: Full EDA on a Messy Dataset

## 🎯 Objective

A stakeholder hands over a messy dataset and asks three things: *what's in here, what can we trust, and what are the three things I should know?* This project delivers a full exploratory data analysis (EDA) notebook plus a one-page insight summary that answers those questions directly.

## 📊 Dataset

**Titanic** — [Kaggle: Titanic – Machine Learning from Disaster](https://www.kaggle.com/c/titanic/data)

`train.csv` contains 891 passenger records with real missingness (`Age`, `Cabin`, `Embarked`) and mixed types (numeric, categorical, and identifier-like text columns), making it a good candidate for practicing profiling, cleaning, and honest data-quality reporting.

> The raw data file is **not committed** to this repository (see `.gitignore`). Download `train.csv` from the Kaggle link above and place it in `data/train.csv` before running the notebook.

## 📂 Repository Structure

```text
week2-challenge/
│
├── README.md
├── requirements.txt
├── .gitignore
├── EDA.ipynb          # Full analysis notebook (profiling → cleaning → EDA → insights)
├── summary.md          # One-page write-up, insights first
└── data/               
    └── train.csv
```

## 🛠️ Setup

1. Clone the repository and navigate into it.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Download `train.csv` from [Kaggle](https://www.kaggle.com/c/titanic/data) and place it at `data/train.csv`.
5. Open and run `EDA.ipynb` top to bottom on a clean kernel.

## 📋 What This Notebook Covers

### Task 1 — Profile the Raw Data
Shape, column names, data types, missing-value counts and percentages, duplicate check, descriptive statistics, target variable distribution, and unique-value counts.

### Task 2 — Clean the Data
Every cleaning decision is paired with a one-line rationale:
- **`Age`** (~20% missing) → imputed with median
- **`Cabin`** (~77% missing) → dropped / flagged (see notebook for exact treatment)
- **`Embarked`** (2 missing) → imputed with mode
- **`Survived`, `Pclass`, `Sex`, `Embarked`** → treated as categorical
- **Outliers** (`Fare`, `SibSp`, `Parch`, `Age`) → identified via IQR, retained as genuine variation
- Duplicate check confirmed with zero duplicate rows

### Task 3 & 4 — Explore and Visualize
At least four labeled visualizations, each answering a specific question:
- Overall survival distribution
- Survival rate by passenger class
- Survival rate by sex
- Survival rate by class + sex combined
- Age distribution by survival status
- Fare distribution by survival status

### Insights
1. **Class + gender interaction is the biggest signal.** Female survival stayed high in 1st/2nd class (96–92%) but fell to 50% in 3rd class, while male survival stayed low (13–37%) across all classes — the two variables interact rather than acting independently.
2. **Age is a weak standalone predictor.** Nearly identical median age (28) for survivors and non-survivors, with heavily overlapping distributions.
3. **Class alone shows a strong survival gradient** — roughly a 39-point spread between 1st class (63%) and 3rd class (24%) survival rates, pointing to socioeconomic access as a major factor.

## 🚀 Capability Gained

Taking a messy dataset from raw to a clear, honest, actionable analysis — the daily work of a data scientist.