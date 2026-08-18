# csvstat-bharat

A lightweight command-line tool for quickly profiling CSV files — get shape, column types, missing values, numeric statistics, and top value counts, all from your terminal.

[![PyPI](https://img.shields.io/badge/pypi-csvstat--bharat-blue)](https://pypi.org/project/csvstat-bharat/0.1.1/)

---

## Features

- 📐 **Shape detection** — rows × columns at a glance
- 🏷️ **Column type inference** — numeric, date, or text
- 🕳️ **Missing value analysis** — count and percentage per column
- 📊 **Numeric statistics** — min, mean, max
- 🔝 **Top value counts** — most frequent values in a column
- ✅ Fully unit-tested with `pytest`

---

## Directory Structure

```
package/
├── .gitignore
├── pyproject.toml              # Build config & package metadata
├── requirements.txt            # Pinned dependencies
├── README.md
│
├── dist/                       # Built artifacts (wheel + sdist)
│   ├── csvstat_bharat-0.1.1-py3-none-any.whl
│   └── csvstat_bharat-0.1.1.tar.gz
│
├── src/
│   └── csvstat/
│       ├── __init__.py         # Package exports
│       ├── cli.py              # argparse-based CLI entry point
│       └── main.py             # Core logic: read_csv, get_shape,
│                                # get_column_type, get_missing_count,
│                                # get_missing_percentage,
│                                # get_numeric_statistics, get_top_values
│
├── tests/
│   └── csvstat-test.py         # pytest unit tests for main.py
│
└── data.csv                    # Sample CSV used for manual testing
```

> **Note:**
> - **`pyproject.toml`** — defines the package metadata (name, version, dependencies) and tells `build`/`pip` how to package and install the project; it's also where the `csvstat` CLI entry point is registered.
> - **`__init__.py`** — marks `csvstat/` as a Python package and re-exports the functions from `main.py` so they can be imported as `from csvstat.main import ...`.
> - **`cli.py`** — the command-line interface layer; uses `argparse` to read the filename/flags typed after `csvstat` and passes them to the functions in `main.py`.

---


**Flow:**
1. User invokes `csvstat data.csv` in the terminal.
2. `cli.py` parses arguments and calls into `main.py`.
3. `main.py` loads the CSV into a pandas `DataFrame` and runs the requested analysis functions.
4. Results are returned to `cli.py`, formatted, and printed to stdout.
5. `tests/csvstat-test.py` independently imports and validates each `main.py` function using `pytest`.

---

## Workflow

1. Write/edit code in `src/csvstat/main.py`
2. Test locally with `pip install -e .` (editable install)
3. Run `pytest tests/csvstat-test.py` to verify nothing broke
4. Bump version in `pyproject.toml`
5. Build with `python -m build`
6. Upload with `twine` (TestPyPI → PyPI)
7. Verify with `pip install csvstat-bharat --upgrade`

---

## 💡 Insight

- **Wheels vs sdists:** when you ran `python -m build`, it produced two files — a `.tar.gz` (source distribution) and a `.whl` (wheel). The wheel is a pre-built, zip-based format that `pip` can install directly without re-running your `setup`/`build` step, which is why wheel installs are noticeably faster than sdist installs.
- **PyPI names are permanent:** once a project name + version (like `csvstat-bharat 0.1.1`) is uploaded to PyPI, it can never be reused — even if you delete it. This is a deliberate anti-supply-chain-attack measure so a malicious package can't later be re-uploaded under a trusted name and version.

---

## Unit Testing

`tests/csvstat-test.py` uses **pytest** to test each function in `main.py` in isolation — each test builds a small in-memory `pandas.DataFrame`, calls one function, and asserts the output.

| Test | What it checks |
|---|---|
| `test_get_shape` | `get_shape()` returns the correct `(rows, columns)` tuple |
| `test_get_column_type_numeric` | A numeric column is correctly identified as `"numeric"` |
| `test_get_column_type_text` | A string column is correctly identified as `"text"` |
| `test_get_column_type_date` | A column with `date` in its name is identified as `"date"` |
| `test_get_missing_count` | Counts `None`/`NaN` values correctly in a column |
| `test_get_missing_percentage` | Calculates missing-value percentage correctly (e.g. 2 of 4 → 50.0%) |
| `test_get_numeric_statistics` | Returns correct `min`, `mean`, `max` for a numeric column |
| `test_get_top_values` | Returns the top N most frequent values as a `{value: count}` dict |

```python
import pandas as pd

from csvstat.main import (
    get_shape,
    get_column_type,
    get_missing_count,
    get_missing_percentage,
    get_numeric_statistics,
    get_top_values,
)


def test_get_shape():
    df = pd.DataFrame({
        "A": [1, 2, 3],
        "B": [4, 5, 6]
    })

    assert get_shape(df) == (3, 2)


def test_get_column_type_numeric():
    df = pd.DataFrame({
        "number": [10, 20, 30]
    })

    assert get_column_type(df, "number") == "numeric"


def test_get_column_type_text():
    df = pd.DataFrame({
        "name": ["A", "B", "C"]
    })

    assert get_column_type(df, "name") == "text"


def test_get_column_type_date():
    df = pd.DataFrame({
        "start_date": ["2025-01-01", "2025-02-01"]
    })

    assert get_column_type(df, "start_date") == "date"


def test_get_missing_count():
    df = pd.DataFrame({
        "value": [10, None, 30]
    })

    assert get_missing_count(df, "value") == 1


def test_get_missing_percentage():
    df = pd.DataFrame({
        "value": [10, None, 30, None]
    })

    assert get_missing_percentage(df, "value") == 50.0


def test_get_numeric_statistics():
    df = pd.DataFrame({
        "value": [10, 20, 30]
    })

    result = get_numeric_statistics(df, "value")

    assert result["min"] == 10
    assert result["mean"] == 20
    assert result["max"] == 30


def test_get_top_values():
    df = pd.DataFrame({
        "city": ["A", "A", "B", "A", "B"]
    })

    result = get_top_values(df, "city", top=2)

    assert result == {
        "A": 3,
        "B": 2
    }
```

Run them with:
```bash
pytest tests/csvstat-test.py
```

---

## Installation

**From PyPI:**
```bash
pip install csvstat-bharat
```

**From source (editable/dev install):**
```bash
cd package
python3.11 -m venv venv
source venv/bin/activate
```

---

## Usage

```bash
csvstat data.csv
```

Or use the core functions directly in Python:

```python
from csvstat.main import read_csv,get_missing_count

df = read_csv("data.csv")

print(df)

stats = get_missing_count(df,"Age")
print(stats)


```
<img width="1372" height="940" alt="image" src="https://github.com/user-attachments/assets/ad30cb38-edb3-4486-8e64-3ca5dfb44fe1" />

---

## Core API (`src/csvstat/main.py`)

| Function | Description |
|---|---|
| `read_csv(file_path)` | Loads a CSV file into a pandas DataFrame |
| `get_shape(df)` | Returns `(rows, columns)` |
| `get_column_type(df, column)` | Returns `"numeric"`, `"date"`, or `"text"` |
| `get_missing_count(df, column)` | Count of missing/null values in a column |
| `get_missing_percentage(df, column)` | Percentage of missing values in a column |
| `get_numeric_statistics(df, column)` | Dict with `min`, `mean`, `max` |
| `get_top_values(df, column, top=N)` | Dict of the N most frequent values and their counts |

---

## Publishing to PyPI

```bash
python -m pip install --upgrade build twine   # installs the build & upload tools
python -m build                               # builds the wheel + sdist into dist/
python -m twine check dist/*                  # validates the build before upload
python -m twine upload --repository testpypi dist/*   # test upload (username: __token__, password: your API token)
python -m twine upload dist/*                          # real upload to PyPI (same credentials)
pip install csvstat-bharat          # verifies the published package installs correctly
```
<img width="985" height="244" alt="image" src="https://github.com/user-attachments/assets/53c800d2-36be-427c-b079-6c5866909acf" />

> Get your API token from [pypi.org/manage/account/token](https://pypi.org/manage/account/token/). Bump the version in `pyproject.toml` before every re-upload — PyPI rejects re-uploading an existing version.

---

## Requirements

- Python 3.11+
- pandas
- numpy
- python-dateutil

---

## Author

**Bharat**
Published on PyPI: [csvstat-bharat](https://pypi.org/project/csvstat-bharat/0.1.1/)