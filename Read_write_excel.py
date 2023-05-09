import pandas as pd

df_data = pd.DataFrame({'States':['Abia', 'Enugu', 'Imo', 'Kaduna', 'Plateau', 'Ebonyi'],
    'Capitals':['Umuahia', 'Enugu', 'Owerri', 'Kaduna', 'Jos', 'Abakalikki'],
    'Population':['508529', '193551', '32315', '619968', '52555', '227032']})

#Extracting the data to Excel.
df_data.to_excel('fridayfile.xlsx', index=False)

# Reading the excel file, fridayfile
Read_file = pd.read_excel('fridayfile.xlsx')
print(Read_file)

