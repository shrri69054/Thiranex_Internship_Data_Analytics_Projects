# 📊 Data Analytics Portfolio

A collection of four end-to-end data analytics projects covering dashboarding, customer segmentation, data automation, and predictive modelling.

---

## 📁 Projects Overview

| Project | Tech Stack | Purpose |
|---|---|---|
| [Sales & Revenue Dashboard](#1-sales--revenue-dashboard) | Python, Streamlit, Plotly, SQL | Interactive sales visualization |
| [Customer Segmentation Analysis](#2-customer-segmentation-analysis) | Python, Scikit-learn, KMeans | ML-based customer clustering |
| [Data Cleaning & Reporting Automation](#3-data-cleaning--reporting-automation) | Python, Pandas, Matplotlib | HR data pipeline & reporting |
| [Predictive Analytics](#4-predictive-analytics-project) | Python, Scikit-learn, Linear Regression | 12-month sales forecasting |

---

## 1. Sales & Revenue Dashboard

An interactive web dashboard for exploring sales and revenue data across products and regions.

### Features
- Upload CSV or Excel sales files directly in the browser
- Filter data by **Region** and **Product** using sidebar controls
- KPI cards for **Total Sales**, **Total Revenue**, and **Average Revenue**
- Interactive charts: Revenue trend (line), Top products (bar), Revenue by region (pie)
- Full data table view

### Project Structure
```
Sales-Revenue-Dashboard/
├── app.py                  # Streamlit application
├── requirements.txt        # Python dependencies
├── data/
│   └── sales_data.csv      # Sample sales dataset
└── sql/
    └── sales_database.sql  # MySQL schema for sales table
```

### Sample Data Format
Your CSV/Excel file should contain these columns:

| Date | Product | Region | Sales | Revenue |
|---|---|---|---|---|
| 2025-01-01 | Laptop | North | 10 | 500000 |

### Setup & Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 2. Customer Segmentation Analysis

A modular Python project that applies **K-Means clustering** to segment customers based on behavioural and demographic features.

### Features
- Data preprocessing with feature scaling (`StandardScaler`)
- K-Means clustering to identify distinct customer groups
- Insight generation per segment
- Visualizations using Matplotlib, Seaborn, and Plotly

### Project Structure
```
customer-segmentation-analysis/
├── main.py                 # Entry point
├── requirements.txt
└── src/
    ├── preprocessing.py    # Data loading & scaling
    ├── clustering.py       # KMeans model
    ├── insights.py         # Segment insight generator
    └── visualization.py    # Charts & plots
```

### Setup & Run
```bash
pip install -r requirements.txt
python main.py
```

### Dependencies
`pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `plotly`, `jupyter`

---

## 3. Data Cleaning & Reporting Automation

An automated Python pipeline that cleans raw employee HR data, generates a department-level summary report, and produces a bar chart — all in one script.

### Features
- Removes duplicate records
- Fills missing `Department` values with `"Unknown"`
- Imputes missing `Salary` and `Performance_Score` with median values
- Exports cleaned data to `cleaned_employee_data.csv`
- Generates a department summary report (`department_report.xlsx`) with:
  - Average salary
  - Average performance score
  - Employee count
- Saves a bar chart of employee distribution as `employee_summary_chart.png`

### Project Structure
```
Data_Cleaning_Reporting_Automation_Project/
├── automation_script.py    # Main pipeline script
└── raw_employee_data.csv   # Input data (Employee_ID, Department, Salary, Performance_Score)
```

### Output Files (generated on run)
| File | Description |
|---|---|
| `cleaned_employee_data.csv` | Deduplicated, imputed employee data |
| `department_report.xlsx` | Department-level summary statistics |
| `employee_summary_chart.png` | Bar chart of employee count by department |

### Setup & Run
```bash
pip install pandas matplotlib openpyxl
python automation_script.py
```

---

## 4. Predictive Analytics Project

A time-series sales forecasting model using **Linear Regression** that predicts the next 12 months of sales from historical data.

### Features
- Parses and sorts historical monthly sales data
- Trains a Linear Regression model on an 80/20 train-test split
- Evaluates model using **MAE**, **RMSE**, and **R² Score**
- Plots historical data vs. test predictions
- Outputs a **12-month future sales forecast**
- Saves prediction chart as `prediction_plot.png`

### Project Structure
```
predictive_analytics_project/
├── predictive_model.py         # Model training, evaluation & forecasting
└── historical_sales_data.csv   # Input: Date, Sales (monthly)
```

### Input Data Format
```
Date,Sales
2020-01-01,103.97
2020-02-01,111.71
...
```

### Output
- Console: MAE, RMSE, R² Score + 12-month forecast values
- File: `prediction_plot.png` — historical vs predicted sales chart

### Setup & Run
```bash
pip install pandas numpy matplotlib scikit-learn
python predictive_model.py
```

---

## 🛠 Prerequisites

- Python 3.8+
- pip

Install all dependencies across projects:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn plotly streamlit openpyxl jupyter
```

---

## 📄 License

This project is for educational and portfolio purposes.
