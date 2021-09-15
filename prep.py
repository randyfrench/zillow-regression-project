import os
import pandas as pd
import numpy as np
from scipy import stats
from env import username, host, password 
from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression

############################## PREP ZILLOW  ##############################

def prep_zillow(df):
    '''
    This function takes in the zillow df acquired by new_zillow_data
    Returns a cleaned zillow df.
    '''
    #create new column for tax_rate
    df['tax_rate'] =(df['tax_amount']/  df['appraised_value']) *100

    #change column names to be more legible
    #df = df.rename(columns={"calculatedfinishedsquarefeet": "total_sqft", "bedroomcnt": "bedrooms", "bathroomcnt": "bathrooms", "taxvaluedollarcnt": "value_assessed", "taxamount": "tax_amount", "yearbuilt": "year_built", "fips": "county_code" })
    
    #replace blank spaces and special characters
    df = df.replace(r'^\s*$', np.nan, regex=True)

    #drop null values- there were 156 
    df = df.dropna()

    #drop duplicates
    df.drop_duplicates(inplace=True)
    
    return df

############################## DROP OUTLIERS FUNCTION ##############################

def remove_outliers(df, k, col_list):
    ''' remove outliers from a list of columns in a dataframe 
        and return that dataframe
    '''
    
    for col in col_list:

        q1, q3 = df[col].quantile([.25, .75])  # get quartiles
        
        iqr = q3 - q1   # calculate interquartile range
        
        upper_bound = q3 + k * iqr   # get upper bound
        lower_bound = q1 - k * iqr   # get lower bound

        # return dataframe without outliers
        
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]
        
    return df
