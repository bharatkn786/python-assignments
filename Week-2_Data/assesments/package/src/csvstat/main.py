import pandas as pd


def read_csv(file_path):
    return pd.read_csv(file_path)


def get_shape(df):
    return df.shape


def get_column_type(df, column):
    if pd.api.types.is_numeric_dtype(df[column]):
        return "numeric"

    elif "date" in column.lower():
        return "date"

    else:
        return "text"


def get_missing_count(df, column):
    return df[column].isna().sum()


def get_missing_percentage(df, column):
    rows = len(df)

    if rows == 0:
        return 0

    missing = df[column].isna().sum()

    return (missing / rows) * 100


def get_numeric_statistics(df, column):
    return {
        "min": df[column].min(),
        "mean": df[column].mean(),
        "max": df[column].max()
    }


def get_top_values(df, column, top=5):
    return df[column].value_counts().head(top).to_dict()