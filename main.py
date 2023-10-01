import pandas as pd
from datetime import timedelta

# Function to load the CSV data into a DataFrame
def load_data(file_name):
    return pd.read_csv(file_name, parse_dates=['Time', 'Time Out'])

# Function to find employees who worked for 7 consecutive days
def find_employees_for_7_consecutive_days(data):
    data.sort_values(['Employee Name', 'Time'], inplace=True)
    data.reset_index(drop=True, inplace=True)

    consecutive_employees = set()

    for i in range(len(data) - 6):
        consecutive_days = data.iloc[i:i + 7]

        if (consecutive_days['Employee Name'].nunique() == 1 and
                (consecutive_days['Time'].iloc[-1] - consecutive_days['Time'].iloc[0]).days == 6):
            employee_name = consecutive_days['Employee Name'].iloc[0]
            consecutive_employees.add(employee_name)

    return consecutive_employees

# Function to find employees with less than 10 hours between shifts but greater than 1 hour
def find_employees_with_less_than_10_hours_between_shifts(data):
    data.sort_values(['Employee Name', 'Time'], inplace=True)
    data.reset_index(drop=True, inplace=True)

    employees_with_less_than_10_hours = set()

    for i in range(len(data) - 1):
        current_row = data.iloc[i]
        next_row = data.iloc[i + 1]

        if (next_row['Employee Name'] == current_row['Employee Name'] and
                (next_row['Time'] - current_row['Time Out']) < timedelta(hours=10) and
                (next_row['Time'] - current_row['Time Out']) > timedelta(hours=1)):
            employee_name = current_row['Employee Name']
            employees_with_less_than_10_hours.add(employee_name)

    return employees_with_less_than_10_hours

# Function to find employees who worked for more than 14 hours in a single shift
def find_employees_with_more_than_14_hours_shift(data):
    data.sort_values(['Employee Name', 'Time'], inplace=True)
    data.reset_index(drop=True, inplace=True)

    employees_with_more_than_14_hours = set()

    for i in range(len(data)):
        shift_hours = (data['Time Out'].iloc[i] - data['Time'].iloc[i]).total_seconds() / 3600

        if shift_hours > 14:
            employee_name = data['Employee Name'].iloc[i]
            employees_with_more_than_14_hours.add(employee_name)

    return employees_with_more_than_14_hours

# Provide the correct file name
input_file = 'assignement_data.csv'

# Load the data from the CSV file
data = load_data(input_file)

# Task 1: Find employees who worked for 7 consecutive days
consecutive_employees = find_employees_for_7_consecutive_days(data)
print("a) Employees who worked for 7 consecutive days:")
for employee in consecutive_employees:
    print(employee)

# Task 2: Find employees with less than 10 hours between shifts but greater than 1 hour
less_than_10_hours_employees = find_employees_with_less_than_10_hours_between_shifts(data)
print("\nb) Employees with less than 10 hours between shifts but greater than 1 hour:")
for employee in less_than_10_hours_employees:
    print(employee)

# Task 3: Find employees who worked for more than 14 hours in a single shift
more_than_14_hours_employees = find_employees_with_more_than_14_hours_shift(data)
print("\nc) Employees who worked for more than 14 hours in a single shift:")
for employee in more_than_14_hours_employees:
    print(employee)
