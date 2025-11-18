#!/usr/bin/env python
# coding: utf-8

# In[22]:


'''
EDA Skeleteon- Personal Modular Workflow
Author: Shailesh Pawar
Version 1.3
Last Updated: Nov 2025
Purpose: Quick Modular EDA on any dataset.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='whitegrid')
cols=["Transaction Amount"]
path=r"C:\Users\Lenovo\OneDrive\Desktop\Github\credit_card_transaction_flow_cleaneddataa.csv"
df = pd.read_csv(path)
def load_data(path, parse_dates=None):
    try:
        
        print("Loaded:", path, "shape:", df.shape)
        return df
    except Exception as e:
        print("Load error:", e)
        raise

def health_check(df,cols):
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("Info:")
    print(df.info())
    print("Missing:\n", df.isnull().sum())
    print("Duplicates:", df.duplicated().sum())
    print("Unique counts:\n", df.nunique())

def coerce_numeric(df, cols):
    for c in cols:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    return df

def basic_stats(df, cols):
    s = df[cols].describe()
    print(s)
    return s

def bar_by_category(df, x="Category", y="Transaction Amount", top_n=10):
    order = df.groupby(x)[y].mean().sort_values(ascending=False).head(top_n).index
    plt.figure(figsize=(8,4))
    sns.barplot(data=df, y=x, x=y, order=order)
    plt.title(f"{y} by {x} (top {top_n})")
    plt.show()
print()
print(load_data(path),health_check(df,cols),coerce_numeric(df, cols),basic_stats(df, cols),
      bar_by_category(df, x="Category", y="Transaction Amount", top_n=10))

# Example usage:
# df = load_data("credit_card_transaction_flow_cleaneddata.csv", parse_dates=['Date'])
# health_check(df)
# df = coerce_numeric(df, ['Transaction Amount'])
# basic_stats(df, 'Transaction Amount')
# bar_by_category(df, 'Category', 'Transaction Amount', top_n=8)


# In[ ]:




