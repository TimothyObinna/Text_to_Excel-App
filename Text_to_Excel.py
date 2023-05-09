import pandas as pd

# Conversion of txt file to CSV
csv_file = pd.read_csv('states.txt', delimiter='\t')

# Conversion of csv file to excel sheet
Excel_file = csv_file.to_excel('output.xlsx', sheet_name='Okechukwu')

if Excel_file:
    print('Not Converted')
else:
    print("")
    print('The Excel file, Output, has been converted successfully.')
    print(" ")
