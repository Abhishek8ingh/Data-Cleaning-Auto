def profile_data(df):
    issues = {}
    issues["total_rows"] = df.shape[0]
    issues["total_columns"] = df.shape[1]

    issues["duplicate_rows"] = df.duplicated().sum()
    issues["null_values"] = df.isnull().sum().to_dict()

    return issues