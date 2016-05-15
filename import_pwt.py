# import workbook 
from openpyxl import load_workbook
penn_table = load_workbook('pwt81.xlsx')

# import sheets
''' in the legend, column A has variable names and column B describes those variables.
' there are rows that do not contain variables
' there are rows that have a descriptor of a group of variables - only column A is filled in these  
'''
legend = penn_table.get_sheet_by_name('Legend')

''' in the data, 
' column A is country code
' column B is country name
' column D is year
' columns E through AU contain data
' row 1 includes variable names in all columns A -> AU
'''
data = penn_table.get_sheet_by_name('Data')

# create per capita variables in data table for selected variables
# GDP (PPP)
# 


# store data in SQLAlchemy database