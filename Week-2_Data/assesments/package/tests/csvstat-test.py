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