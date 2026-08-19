# Weekly Challenge: Full EDA on a Messy Dataset — Summary

**Dataset:** Titanic (`train.csv`) — Kaggle *Titanic: Machine Learning from Disaster*

**Objective:** Profile the raw Titanic dataset, clean it with justified decisions, explore key survival patterns, and surface actionable insights and modeling risks.

---
# Titanic EDA — Dataset Summary

The Titanic dataset contains **891 passengers and 12 columns** covering passenger details, class, age, fare, family information, gender, and survival. The main data-quality issues were missing values in `Cabin` (~77%), `Age` (~20%), and `Embarked` (~0.2%). No duplicate records were found.

The dataset was cleaned by imputing missing `Age` values with the median, filling missing `Embarked` values with the mode, and dropping the highly incomplete `Cabin` column. Potential outliers in `Fare`, `Age`, `SibSp`, and `Parch` were retained because they appeared to represent legitimate passenger variation rather than data errors.

The analysis found that **gender and passenger class were the strongest factors associated with survival**. Female passengers had a much higher survival rate than males, while survival also decreased substantially from first to third class. The combination of gender and class revealed an even stronger pattern. In contrast, **age showed only a weak relationship with survival**, with both survivors and non-survivors having a median age of 28.

Overall, the analysis suggests that **gender and passenger class were strongly associated with survival**, while age alone was not a strong separator. A key modeling risk is the high level of missingness in `Cabin`, which makes direct use or imputation of that variable unreliable.

## Task 1: Profiling the Raw Data

- **Shape:** 891 rows × 12 columns
- **Data types:** Mostly correctly typed (`int64`, `float64`, `str`), but `Survived` and `Pclass` are stored as integers even though they represent categories, not quantities
- **Missing values:**
  | Column | Missing | % |
  |---|---|---|
  | `Cabin` | 687 | ~77% |
  | `Age` | 177 | ~20% |
  | `Embarked` | 2 | ~0.2% |
- **Duplicates:** None found
- **Target variable (`Survived`):** 549 did not survive, 342 survived (~38.4% survival rate) — moderately imbalanced classes
- **High-cardinality columns:** `PassengerId`, `Name`, `Ticket` — identifier-like, little standalone predictive value

---

## Task 2: Cleaning the Dataset

| Column | Issue | Decision | Rationale |
|---|---|---|---|
| `Age` | ~20% missing | Imputed with median (28.0) | Reduces influence of extreme values while retaining observations |
| `Cabin` | ~77% missing | Dropped column entirely | Too sparse to impute reliably without fabricating data |
| `Embarked` | 2 missing | Imputed with mode (`S`) | Only 2 rows affected — low-risk categorical fill |
| `Survived`, `Pclass`, `Sex`, `Embarked` | Stored as numeric/object | Treated as categorical | Prevents these being mistakenly used as continuous measures |
| Outliers (`Fare`, `SibSp`, `Parch`, `Age`) | Flagged via IQR | Retained, not removed | Represent genuine large families / high fares, not data errors |

**Post-cleaning shape:** 891 rows × 11 columns (after dropping `Cabin`), 0 missing values, 0 duplicates.

> **Note:** An earlier draft mentioned engineering a `HasCabin` flag before dropping `Cabin`, but the final executed cleaning steps only show the column being dropped outright — worth double-checking your own notebook to confirm which approach you actually implemented.

---

## Task 3: Exploratory Data Analysis

- **Survival distribution:** 38.4% survived overall
- **Correlation with `Survived`** (strongest to weakest):
  1. `Sex` (encoded) → **+0.54** (strongest predictor)
  2. `Fare` → +0.26
  3. `Pclass` → **-0.34** (higher class number = lower survival)
  4. `Parch`, `SibSp`, `Age` → weak correlations (~±0.03–0.08)

---

## Task 4: Visualization Highlights

- **By class:** Survival rate drops steadily from 1st (63%) → 2nd (47%) → 3rd (24%) class
- **By sex:** Female survival (74.2%) far exceeds male survival (18.9%)
- **By class + sex combined:**
  | Class | Female | Male |
  |---|---|---|
  | 1st | 96.8% | 36.9% |
  | 2nd | 92.1% | 15.7% |
  | 3rd | 50.0% | 13.5% |
- **Age vs. survival:** Median age identical (28) for both groups — age alone doesn't separate survivors from non-survivors
- **Fare vs. survival:** Survivors paid a notably higher median fare (26.0) vs. non-survivors (10.5)

---

## Key Findings

1. **Class + gender interaction is the biggest signal.** Female survival stayed high in 1st/2nd class (96–92%) but fell to 50% in 3rd class, while male survival stayed low (13–37%) across all classes — the two variables interact rather than acting independently.
2. **Age is a weak standalone predictor.** Nearly identical median age (28) for survivors and non-survivors, with heavily overlapping distributions.
3. **Class alone shows a strong survival gradient** — roughly a 39-point spread between 1st class (63%) and 3rd class (24%) survival rates, pointing to socioeconomic access as a major factor.

## Data-Quality / Modeling Risk

`Cabin` is ~77% missing — too sparse to use or impute directly. Since the missingness pattern itself may carry signal (e.g., correlating with fare/class), it's safer to capture that as a `HasCabin` indicator than to invent cabin values or drop the signal entirely.