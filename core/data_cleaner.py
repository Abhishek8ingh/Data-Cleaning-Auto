import pandas as pd

def clean_data(df):
    summary = {}

    original_rows = df.shape[0]

    # Remove duplicates
    duplicate_count = df.duplicated().sum()
    df = df.drop_duplicates()

    # Handle null values
    null_before = df.isnull().sum().sum()

    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].str.strip()
            df[column].fillna(df[column].mode()[0], inplace=True)
        else:
            df[column].fillna(df[column].median(), inplace=True)

    null_after = df.isnull().sum().sum()

    summary["rows_before"] = original_rows
    summary["rows_after"] = df.shape[0]
    summary["duplicates_removed"] = duplicate_count
    summary["null_before"] = null_before
    summary["null_after"] = null_after

    return df, summary
