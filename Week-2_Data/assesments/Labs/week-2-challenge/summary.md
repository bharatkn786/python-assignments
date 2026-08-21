# Titanic EDA — Key Insights

## Insights

1. **Class + gender interaction is the biggest signal.** Female survival stayed high in 1st/2nd class (96–92%) but fell to 50% in 3rd class, while male survival stayed low (13–37%) across all classes — the two variables interact rather than acting independently.

2. **Age is a weak standalone predictor.** Nearly identical median age (28) for survivors and non-survivors, with heavily overlapping distributions.

3. **Class alone shows a strong survival gradient.** Survival was approximately 63% in 1st class compared with 24% in 3rd class — a roughly 39-percentage-point difference, pointing to socioeconomic access as a major factor.

## Supporting Evidence

- **Female survival:** 74.2%
- **Male survival:** 18.9%
- **1st-class survival:** 63%
- **2nd-class survival:** 47%
- **3rd-class survival:** 24%
- **Median age:** 28 for both survivors and non-survivors
- **Median fare:** 26.0 for survivors vs. 10.5 for non-survivors

### Class + Gender

| Class | Female | Male |
|---|---:|---:|
| 1st | 96.8% | 36.9% |
| 2nd | 92.1% | 15.7% |
| 3rd | 50.0% | 13.5% |

## Data Quality / Modeling Risk

`Cabin` is approximately **77% missing**, making direct imputation unreliable. `Age` is approximately **20% missing**, while only two `Embarked` values are missing. No duplicate records were found.

Potential outliers in `Fare`, `Age`, `SibSp`, and `Parch` were retained because they appeared to represent legitimate passenger variation rather than obvious data errors.

## Conclusion

The analysis shows that **gender and passenger class were the strongest factors associated with Titanic survival**. Their combination reveals the clearest pattern: women, particularly those in higher passenger classes, had substantially higher survival rates, while men and 3rd-class passengers had much lower rates. **Age showed little standalone separation**, making it a weaker signal in this dataset.

The findings are useful for understanding survival patterns, but the high level of missingness in `Cabin` remains an important modeling limitation.