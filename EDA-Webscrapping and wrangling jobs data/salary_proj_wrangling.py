# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 19:20:06 2021

@author: Deb
"""

import pandas as pd
import numpy as np

df = pd.read_csv("F:\GIT\ds_salary_proj\salary_data_cleaned.csv")

def title_simplifier(title):
    if 'data scientist' in title.lower():
        return 'data scientist'
    elif 'data engineer' in title.lower():
        return 'data engineer'
    elif 'analyst' in title.lower():
        return 'analyst'
    elif 'machine learning' in title.lower():
        return 'machine learning'
    elif 'data architect' in title.lower():
        return 'data architect'
    elif 'manager' in title.lower():
        return 'manager'
    elif 'director' in title.lower():
        return 'director'
    else:
        return 'na'
    
def seniority(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'lead' in title.lower() or 'principal' in title.lower():
        return 'senior'
    elif 'jr' in title.lower() or 'junior' in title.lower() or 'jr.' in title.lower():
        return 'junior'
    else:
        return 'na'
    

df['job_simplifier'] = df['Job Title'].apply(title_simplifier)
df.job_simplifier.value_counts()

df['seniority'] = df['Job Title'].apply(seniority)
df.seniority.value_counts()

df.Job_State.value_counts()

df['State'] = df.Job_State.apply(lambda x: x.strip() if x.strip().lower() != 'los angeles' else 'CA')
df.drop('Job_State', axis=1, inplace=True)

df.State.value_counts()
df.columns

df['desc_len'] = df['Job Description'].apply(lambda x: len(x))

df['comp_cnt'] = df['Competitors'].apply(lambda x: len(x.split(',')) if x != '-1' else 0)

# Hourly salary treatment

#df.drop(['min_salary1', 'max_salary1'], axis=1, inplace=True)
df['min_salary'] = df.apply(lambda x: x.min_salary*2 if x.hourly == 1 else x.min_salary, axis=1)
df['max_salary'] = df.apply(lambda x: x.max_salary*2 if x.hourly == 1 else x.max_salary, axis=1)

df['Company_txt'] = df['Company_txt'].apply(lambda x: x.replace('\n',''))

df.to_csv('salary_data_cleaned_1.csv',index=False)



