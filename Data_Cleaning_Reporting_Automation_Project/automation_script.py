import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('raw_employee_data.csv')
df = df.drop_duplicates()
df['Department'] = df['Department'].fillna('Unknown')
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
df['Performance_Score'] = df['Performance_Score'].fillna(df['Performance_Score'].median())

df.to_csv('cleaned_employee_data.csv', index=False)

report = df.groupby('Department').agg({
    'Salary':'mean',
    'Performance_Score':'mean',
    'Employee_ID':'count'
}).rename(columns={'Employee_ID':'Employee_Count'})

report.to_excel('department_report.xlsx')

report['Employee_Count'].plot(kind='bar')
plt.tight_layout()
plt.savefig('employee_summary_chart.png')
print(report)
