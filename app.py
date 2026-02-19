import streamlit as st
import pandas as pd
from core.data_loader import load_data
from core.data_profiler import profile_data
from core.data_cleaner import clean_data
from core.report_generator import generate_report

st.title("🧹 CSV Data Cleaning Automation")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:

    df = load_data(uploaded_file)

    st.subheader("Raw Data Preview")
    st.dataframe(df.head())

    issues = profile_data(df)

    st.subheader("Issues Found")
    st.write(f"Duplicate Rows: {issues['duplicate_rows']}")
    st.write(f"Total Null Values: {sum(issues['null_values'].values())}")

    # Clean Data Button
    if st.button("Clean Data"):
        cleaned_df, summary = clean_data(df)
        report = generate_report(summary)

        # Save in session state
        st.session_state.cleaned_df = cleaned_df
        st.session_state.report = report

    # Show results if already cleaned
    if "cleaned_df" in st.session_state:

        st.subheader("Cleaned Data Preview")
        st.dataframe(st.session_state.cleaned_df.head())

        st.download_button(
            label="Download Cleaned CSV",
            data=st.session_state.cleaned_df.to_csv(index=False),
            file_name="cleaned_data.csv",
            mime="text/csv"
        )

        st.download_button(
            label="Download Cleaning Report",
            data=st.session_state.report,
            file_name="cleaning_report.txt",
            mime="text/plain"
        )
