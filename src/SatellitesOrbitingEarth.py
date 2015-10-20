#!/usr/bin/python
''' The data of all of the satellites orbiting the Earth was 
acquired from the UCS Satellite Database located at:
www.ucsusa.org/satellite_database
The version used here is the most recent'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xlrd
#import ExtractSatellitesOrbitingEarth


'''#Read in the data from the excel file
wb = xlrd.open_workbook('UCS_Satellite_Database_MostRecent.xlsx')
#Get first sheet
first_sheet = wb.sheet_by_index(0)
print first_sheet.row_values(0)
print first_sheet.cell(0,0) '''

data = pd.ExcelFile("UCS_Satellite_Database_MostRecent.xlsx")
#print(data.sheet_names)
df = data.parse("Sheet1")
print(df.head)





