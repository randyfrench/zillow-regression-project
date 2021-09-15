
# Zillow - Predicting Tax Values of Single Unit Properties - May-August 2017


## Goals:

- Predict the values of single unit properties based on sold data from May-August of 2017
- Identify the county & state where the properties are located in addition to the distribution of property tax rates

******************************************************************************************
## Data Dictionary:

| Feature           | Datatype                | Definition   |
|:------------------|:------------------------|:-------------|
| parcelid          | 28264 non-null: int64   |unique poperty id|
| sqft_calc         | 28264 non-null: int64   |Calculated Square footage of residence |
| bathrooms         | 28264 non-null: int64   |Number of bathrooms in residence   |
| bedrooms          | 28264 non-null: int64   |Number of Bedrooms in residence | 
| appraised_value   | 28264 non-null: int64   |The estimated value of the home|
| year_built        | 28264 non-null: float64 |The year the home was built |
| region_id_county  | 28264 non-null: float64 |The county code of where the property is located|
| tax_amount        | 28264 non-null: float64 |The amount of taxes payed the previous year (2016) |
| county            | 28264 non-null: object  |County the resident resides|
| region_id_zip     | 28264 non-null: float64 |The zip code the poperty is located|
| tax_rate          | 28264 non-null: float64 |The tax rate the resident was charged at|

**********************************************************************

## Pipeline Stages Breakdown

### Acquire

- Store functions that are needed to acquire data from the Zillow database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.

- The final function will return a pandas DataFrame.

- Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.

- Complete some initial data summarization (.info(), .describe(), .value_counts(), ...).

*****************************************************************
### Prepare

- Store functions needed to prepare the Zillow data; make sure the module contains the necessary imports to run the code.

- The final function should do the following:
    - creates tax_rate column
    - change column names to make them more legible
    - remove any duplicates
    - removes outliers

- Import the prep function from the prep.py module and use it to prepare the data in the Final Report Notebook.

*****************************************************

### Explore

- Answer key questions, my hypotheses, and figure out the features that can be used in a regression model to best predict the target variable, appraised_value.

- Run statistical tests in data exploration:
    - Document my hypotheses
    - set an alpha before running the test
    - document the findings



- Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.
************************

### Model

- Establish a baseline accuracy to determine which model performs better than the baseline (if any)
- Train (fit, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
- Compare evaluation metrics across all the models I trained
- Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
- Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.

***************************
### Deliver

- 5 minute presentation that is verbally supported by slides
    - Audience: Zillow Data Science Team (use technical language)
    - highlights of analysis from pipeline
    - Takeaways from visuals in explore
- Github repository with final notebook that has full data science pipeline, acquire.py, and prep.py
- Readme.md file that documents all steps for project reproducibility, data dictionary, goals and key findings/takeaways

Reproduce My Project

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook.

- Read this README.md
- Download the aquire.py, prepare.py, and final_report.ipynb files into your working directory
- Add your own env file to your directory. (user, password, host)
- Run the zillow_final_regression.ipynb notebook

