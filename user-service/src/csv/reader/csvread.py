import pandas
df = pandas.read_csv('../../../resources/employee.csv', index_col='Name', parse_dates=['Hire Date'])
print(df)