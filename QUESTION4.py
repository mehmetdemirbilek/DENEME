#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 23:52:24 2023

@author: mehmetdemirbilek
"""

import pandas as pd

# Read the data
data = pd.read_csv('/Users/mehmetdemirbilek/Downloads/country_vaccination_stats.csv')

# Group the data by country
grouped = data.groupby('country')

# Define a function to impute missing data
def impute_missing(group):
    # Find the minimum daily vaccinations among relevant countries
    relevant_countries = group['vaccines'].str.cat(sep=',').split(',')
    relevant_data = data[data['country'].isin(relevant_countries)]
    min_vaccinations = relevant_data['daily_vaccinations'].min()

    # Fill missing values with the minimum daily vaccinations
    group['daily_vaccinations'] = group['daily_vaccinations'].fillna(min_vaccinations if not pd.isna(min_vaccinations) else 0)
    return group

# Apply the function to each group
imputed_data = grouped.apply(impute_missing)

# Save the imputed data to a new CSV file
imputed_data.to_csv('vaccinations_imputednew.csv', index=False)
