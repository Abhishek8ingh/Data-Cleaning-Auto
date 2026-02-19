def generate_report(summary):
    report = f"""
DATA CLEANING REPORT
---------------------

Rows Before Cleaning: {summary['rows_before']}
Rows After Cleaning: {summary['rows_after']}

Duplicate Rows Removed: {summary['duplicates_removed']}

Null Values Before Cleaning: {summary['null_before']}
Null Values After Cleaning: {summary['null_after']}
"""

    return report
