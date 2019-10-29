'''
lambdata - a collection of data science helper functions
'''

import pandas as pd
import numpy as np

# # sample code
# ONES = pd.DataFrame(np.ones(10))
# ZEROS = pd.DataFrame(np.zeros(50))

# helper functions

def c_nan(df):
    #return nan count in dataframe format
    return pd.DataFrame({"NaN Count Per Column":df.isna().sum()})

def df_stats(dataframe):
    #returns shape, default head(),NaN sum per column,dtypes,describe, and value counts per column
    display(dataframe.shape,dataframe.head(),dataframe.isna().sum(),dataframe.dtypes,dataframe.describe(include="all"))
    for column in dataframe:
        display(dataframe[column].value_counts())

def h(dataframe,*args):
    #returns head() with optional row specification
    return display(dataframe.head(*args),dataframe.shape)

 def df_valcounts(df):
    #helper function to view value_counts for all non number features in a dataframe.
    object_cols = df.select_dtypes(exclude='number')
    for col in object_cols:
        print(df[col].value_counts(normalize=True))

def val_other(X,top):
    # When object columns values beyond the top X highest frequency, replace with "OTHER" value 
    object_cols = X.select_dtypes(exclude='number')
    for col in object_cols.columns:
        if X[col].nunique() >= (top):
            topnumber = X[col].value_counts()[:top].index
            X.loc[~X[col].isin(topnumber), col] = "OTHER"
    return X

def add_l(df,l,col_name):
    # function to take a list and add to dataframe specifying column name
    df[col_name] = l


    
