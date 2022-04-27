#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 10:59:14 2022

@author: tomhollerbach
"""

import pandas as pd
import statsmodels.formula.api as sm

ransomware = pd.read_excel(r'/Users/tomhollerbach/Desktop/MSBA/RansomwareRepository_v11.7.xlsx')
ransomware.dropna(subset=['PaidStatus'], inplace=True)
ransomware = ransomware.replace({'PaidStatus': {'Yes': 1, 'No': 0, 'yes': 1}})

ransomware.isna().sum()

x = ransomware.groupby(['Primary CI Sector targeted']).PaidStatus.value_counts(normalize=True)
x = x.to_frame()
x = x[x.PaidStatus != 0]


#model  = sm.ols(formula='PaidStatus ~ ', data = ransomware).fit()
#print(model.summary())

ransomware['Primary CI Sector targeted'].value_counts()
ransomware['PaidStatus'].value_counts()
ransomware['Location (State)'].value_counts()

column_1 = ransomware["Year"]
column_2 = ransomware["PaidStatus"]
correlation = column_1.corr(column_2)

df = ransomware[["Ransom Amount", "Local Currency", "PaidStatus", "AmtPaid"]].copy()
df = df[df.PaidStatus != 0]
df.isna().sum()

df1 = ransomware[["Date_Began", "Year", "OrgName", "Primary CI Sector targeted", "Location (State)", "PaidStatus", "Source"]].copy()
df1.isna().sum()
df1.dropna(inplace=True)

df1['Site']=df1['Source'].str.extract('\/\/(.+?)\/')
df1['Site'] = df1.Site.str.replace('www.', '')
x = df1['Site'].value_counts()





