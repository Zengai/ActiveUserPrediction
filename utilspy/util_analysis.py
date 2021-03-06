import pandas as pd
import numpy as np
def missing_values_table(df):
    """Function to calculate missing values by column"""
    # Total missing values
    mis_val = df.isnull().sum()

    # Percentage of missing values
    mis_val_percent = 100 * df.isnull().sum() / len(df)

    # Make a table with the results
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)

    # Rename the columns
    mis_val_table_ren_columns = mis_val_table.rename(
        columns={0: 'Missing Values', 1: '% of Total Values'})

    # Sort the table by percentage of missing descending
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:, 1] != 0].sort_values(
        '% of Total Values', ascending=False).round(3)

    # Print some summary information
    print("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"
                                                              "There are " + str(mis_val_table_ren_columns.shape[0]) +
          " columns that have missing values.")
    # Return the dataframe with missing information
    return mis_val_table_ren_columns
# Function to calculate correlations with the target for a dataframe
def target_corrs(df,target="label",method="pearson"):
    # List of correlations
    corrs = []

    # Iterate through the columns
    for col in df.columns:
        # print(col)
        # Skip the target column
        if col != target:
            # Calculate correlation with the target
            corr = df[target].corr(df[col],method=method)
            print('The correlation between %s and the TARGET is %0.4f' % (col, corr))
            # Append the list as a tuple
            corrs.append((col, corr))

    # Sort by absolute magnitude of correlations
    corrs = sorted(corrs, key=lambda x: abs(x[1]), reverse=True)

    return corrs
# Function to calculate mutual information with the target for a dataframe
def target_mi(df,target="label"):
    from sklearn.feature_selection import mutual_info_classif
    # List of correlations
    mis = []

    # Iterate through the columns
    for col in df.columns:
        # print(col)
        # Skip the target column
        if col != target:
            # Calculate correlation with the target
            mi = mutual_info_classif(df[col].values,df[target].values)[0]
            print('The mutual information  between %s and the TARGET is %0.4f' % (col, mi))
            # Append the list as a tuple
            mis.append((col, mi))

    # Sort by absolute magnitude of correlations
    corrs = sorted(mi, key=lambda x: abs(x[1]), reverse=True)

    return corrs


