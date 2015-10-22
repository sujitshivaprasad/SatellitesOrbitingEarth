#!/usr/bin/python
''' The data of all of the satellites orbiting the Earth was 
acquired from the UCS Satellite Database located at:
www.ucsusa.org/satellite_database
The version used here is the most recent'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xlrd 
import xlwt
#import ExtractSatellitesOrbitingEarth

#data = pd.ExcelFile("UCS_Satellite_Database_MostRecent.xlsx")
#print(data.sheet_names)
#df = data.parse("Sheet1")
#print(df.head)

workbook = xlrd.open_workbook('UCS_Satellite_Database_MostRecent.xls', on_demand = True)
worksheet = workbook.sheet_by_index(0) #I think UCS usually uses only sheet 1 for their data

max_rows = worksheet.nrows #max rows in sheet
max_cols = worksheet.ncols #max columns in sheet
IndiaNum = []; USANum = []

for i in range(0, max_rows):
	if worksheet.cell(i,1).value == 'India':
		#print('Found!', i+1)
		IndiaNum.append(i+1) #All of India's satellite cell values
	elif worksheet.cell(i,1).value == 'USA':
		USANum.append(i+1) #All of USA's satellite cell values

NumIndia = len(IndiaNum) #Count India's satellites
NumUSA = len(USANum) #Count USA's satellites








