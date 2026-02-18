# Data-Cleaning-Auto

A simple automation tool built using Python and Streamlit that cleans messy CSV datasets automatically and generates a data cleaning report.

This project allows users to upload a raw CSV file, detect common data issues, clean the dataset, and download both the cleaned dataset and the cleaning report.

------------------------------------------------------------

🚀 FEATURES (Version 1)

- Upload CSV file through a simple UI
- Detect duplicate rows
- Detect null values
- Remove duplicate rows automatically
- Fill missing values:
  - Numeric columns → Median
  - Categorical columns → Mode
- Strip extra spaces from text columns
- Preview raw and cleaned data
- Download:
  - Cleaned CSV file
  - Cleaning report (.txt)

------------------------------------------------------------

📁 PROJECT STRUCTURE

data_cleaning_automation/
│
├── app.py
│
├── core/
│   ├── __init__.py
│   ├── data_cleaner.py
│   ├── data_loader.py
│   ├── data_profiler.py
│   ├── report_generator.py
│
└── output_data/   (Currently not used in Version 1)

------------------------------------------------------------

🧠 HOW IT WORKS

1. Upload a CSV file.
2. The system profiles the dataset.
3. It detects:
   - Duplicate rows
   - Missing values
4. Click "Clean Data".
5. The system:
   - Removes duplicates
   - Fills null values
   - Cleans text columns
6. Download:
   - Cleaned dataset
   - Cleaning report

------------------------------------------------------------

📌 CURRENT VERSION LIMITATIONS

- No advanced data type correction
- No outlier detection
- No configurable cleaning options
- output_data folder is not yet used for automatic saving
- No requirements.txt file (will be added in next version)

------------------------------------------------------------

🔮 FUTURE IMPROVEMENTS

- User-controlled cleaning options
- Outlier detection
- Data type standardization
- Automatic saving in output_data folder
- requirements.txt file
- Logging system
- Data visualization dashboard
- Config file support

------------------------------------------------------------

🛠️ TECHNOLOGIES USED

- Python
- Pandas
- NumPy
- Streamlit

------------------------------------------------------------

🎯 PURPOSE OF THIS PROJECT

This project is built to practice:

- Data cleaning workflows
- Modular project structure
- Streamlit application development
- Automation of repetitive data tasks
