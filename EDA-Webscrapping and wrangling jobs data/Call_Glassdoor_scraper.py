# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 12:52:38 2021

@author: Deb
"""

import Glassdoor_scraper as gs
#import pandas as pd

path='F:/GIT/ds_salary_proj/chromedriver'

df = gs.get_jobs('data scientist', 5, False, path, 15)