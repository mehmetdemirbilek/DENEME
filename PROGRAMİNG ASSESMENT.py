#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 01:13:05 2023

@author: mehmetdemirbilek
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('/Users/mehmetdemirbilek/Downloads/dataset.csv')

print(df.head())
print(df.info())
print(df.describe())

sns.pairplot(df, hue='isVirus')
plt.show()

virus_df = df[df['isVirus'] == True]
non_virus_df = df[df['isVirus'] == False].sample(n=len(virus_df), random_state=42)
balanced_df = pd.concat([virus_df, non_virus_df]).reset_index(drop=True)

imputer = SimpleImputer(strategy='mean')
X = balanced_df.drop(columns=['isVirus'])
y = balanced_df['isVirus']
X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

sns.pairplot(X_imputed, diag_kind='hist')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, cmap='Blues')
plt.xlabel('Predicted label')
plt.ylabel('True label')
plt.show()
