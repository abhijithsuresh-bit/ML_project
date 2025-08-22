import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns',None) # this is used to display all the columns in a excel

patient_df=pd.read_excel('C:/Users/ASUS TUFF/Desktop/ML_project/Patient_Characteristics_Survey__PCS___2019.csv.xlsx',dtype={"Unknown Chronic Med Condition": str}) # here we use pd.read_excel because last extention is .xlsx
patient_df.head(5)

patient_df[patient_df.duplicated()]

patient_df=patient_df.drop_duplicates()

(patient_df['Age Group']=='CHILD').sum() #to get the value of a single value

patient_df=patient_df[patient_df['Mental Illness']!='UNKNOWN']

# Filter rows where 'Mental Illness' is 'YES'
filtered_rows = patient_df[patient_df['Mental Illness'] == 'YES']

# Select columns from start up to 'Mental Illness'
result = filtered_rows.loc[:, :'Mental Illness']

# Display the result
result


