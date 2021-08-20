# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 23:21:54 2021

@author: Deb
"""

import pandas as pd

df = pd.read_csv("glassdoor_jobs.csv")

#Salary treatment

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate']!='-1']

df1 = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
df2 = df1.apply(lambda x: x.replace('$','').replace('K',''))

df3 = df2.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = df3.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = df3.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#df.drop(['min_salary','max_salary','avg_salary'], axis=1, inplace=True)

# Company Name treatment

df['Company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating']<1 else x['Company Name'][:-3], axis=1)

# Location treatment to get state only

df['Job_State'] = df['Location'].apply(lambda x: x.split(',')[1])
df.Job_State.value_counts()

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1)
# Age of Company
#df.drop('Age',axis=1,inplace=True)
df['Age'] = df['Founded'].apply(lambda x: x if x<0  else 2021-x)

# Job description

df['Python_R'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() or ' r ' in x.lower() or 'r-studio' in x.lower() or 'r studio' in x.lower() else 0)
#df.drop('Python',axis=1,inplace=True)
df['Spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['SAS'] = df['Job Description'].apply(lambda x: 1 if 'sas' in x.lower() else 0)
df['Cloud'] = df['Job Description'].apply(lambda x: 1 if 'cloud' in x.lower() else 0)
df['Excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

df.Excel.value_counts()
df.SAS.value_counts()
df.Cloud.value_counts()

df.columns

df.drop('Unnamed: 0',axis=1,inplace=True)

df.to_csv('salary_data_cleaned.csv',index=False)

#df_test = pd.read_csv('salary_data_cleaned.csv')
