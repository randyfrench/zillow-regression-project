#import libraries
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Connection
from env import host, user, password

# Acquire Zillow Data

# Create function to get the necessary connection url.
def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db. It takes in a string 
    name of a database as an argument
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


#create function to retrieve zillow data
def new_zillow_data():
    '''
    This function reads the Telco data from the Codeup db
    and returns a pandas DataFrame with three joined tables and all columns.
    '''
    
    sql_query = '''
    SELECT parcelid, bedroomcnt AS bathrooms, bathroomcnt as bedrooms, calculatedfinishedsquarefeet AS sqft_calc, 
           taxvaluedollarcnt AS appraised_value, assessmentyear AS assessment_year, 
           taxamount AS tax_amount, fips AS county, yearbuilt AS year_built, regionidcounty AS region_id_county,
           regionidzip AS region_id_zip, transactiondate AS transaction_date
    FROM properties_2017
        JOIN predictions_2017 USING(parcelid)
            JOIN propertylandusetype USING (propertylandusetypeid)
    WHERE transactiondate BETWEEN "2017-05-01" AND "2017-08-31"
        AND propertylandusetypeid IN (261, 262, 263, 264, 265, 268, 273, 275, 276, 279); 
    '''
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('zillow'))
    
    return df

# this is to cache a csv file of the data from the db for a quicker read
def get_zillow_data():
    '''
    checks for existing csv file
    loads csv file if present
    if there is no csv file, calls new_zillow_data
    '''
    
    if os.path.isfile('zillow.csv'):
        
        df = pd.read_csv('zillow.csv', index_col=0)
        
    else:
        
        df = new_zillow_data()
        
        df.to_csv('zillow.csv')

    return df


def get_data_summary(df):
    '''
    This function takes in a pandas dataframe and prints out the shape of the dataframe, number of missing values, 
    columns and their data types, summary statistics of numeric columns in the dataframe, as well as the value counts for categorical variables.
    '''
    # Print out the "shape" of our dataframe - the rows and columns we have to work with
    print(f'The zillow dataframe has {df.shape[0]} rows and {df.shape[1]} columns.')
    print('')
    print('-------------------')

    # print the number of missing values in our dataframe
    print(f'There are total of {df.isna().sum().sum()} missing values in the entire dataframe.')
    print('')
    print('-------------------')

    # print some information regarding our dataframe
    df.info()
    print('')
    print('-------------------')
    
    # print out summary stats for our dataset
    print('Here are the summary statistics of our dataset')
    print(df.describe())
    print('')
    print('-------------------')

    print('Here are the categories and their relative proportions')
    # check different categories and proportions of each category for object type cols
    show_vc = ['county','bathrooms','bedrooms', 'year_built']
    for col in df.columns:
        if col in show_vc:
            print(f'value counts of {col}')
            print(df[col].value_counts())
            print('')
            print(f'proportions of {col}')
            print(df[col].value_counts(normalize=True,dropna=False))
            print('-------------------')


