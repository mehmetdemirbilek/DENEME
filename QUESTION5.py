#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 00:06:21 2023

@author: mehmetdemirbilek
"""

import pandas as pd

# Read the data
data = pd.read_csv('/Users/mehmetdemirbilek/Downloads/country_vaccination_stats.csv')



# Compute the median daily vaccinations per country
medians = data.groupby('country')['daily_vaccinations'].median()

# Get the top-3 countries with the highest median daily vaccinations
top3 = medians.nlargest(3)

# Print the result
print(top3)