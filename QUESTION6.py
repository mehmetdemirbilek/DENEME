#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 00:11:28 2023

@author: mehmetdemirbilek
"""

import pandas as pd

# Read the data
data = pd.read_csv('/Users/mehmetdemirbilek/Downloads/country_vaccination_stats.csv')


# Filter the data for the date 1/6/2021
date = '1/6/2021'
filtered = data[data['date'] == date]

# Compute the total vaccinations for the date
total_vaccinations = filtered['daily_vaccinations'].sum()

# Print the result
print("Total vaccinations on", date, ":", total_vaccinations)