# ----------------------------------------------------------------------
# Name:        lecture24
# Purpose:     Demonstrate the use of Pandas
#
# Author:      Ian SooHoo
# ----------------------------------------------------------------------
"""
Skeleton module to be used in lecture 24.


"""
import pandas as pd
import numpy as np
import re

def q1(df):
    """
   How many rows
    """
    return len(df)

def q2(df):
    """
   Unique species by Scientific Name are there
    """
    return len(df['Scientific Name'].unique())

def q3(df):
    """
   Unique species by Scientific Name are there
    """
    return len(df[df['Conservation Status'] == 'Endangered'])

def q4(df):
    """
   Native and threatened species
    """
    return len(df[(df['Conservation Status'] == 'Endangered')
            & (df['Nativeness'] == 'Native')])

def q5(df):
    """
   Bird species and concern
    """
    return len(df[(df['Category'] == 'Bird')
            & (df['Conservation Status'] == 'Species of Concern')])

# def q6(df):
#     """
#    Fish species (common name are theatened in yosemite
#    Must use loc because we are projecting a column
#    project on common names
#     """
#     return df.loc[(df['Conservation Status'] == 'Threatened') &
#         (df['Category'] == 'Fish') &
#         (df['Park Name'] == 'Yosemite National Park'), "Common Names"]

# def q7(df):
#     """
#    Where can we find bears
#    Must use loc because we are projecting a column
#    project on common names
#     """
#     return df.loc[(df['Common Names'].str.contans(r'\Bear\b',
#                                                   flags=re.IGNORECASE)) &
#                   df["Category"] == "Mammal", "Park Name"]


def q8(df):
    """
   Where can we find bears
   Must use loc because we are projecting a column
   project on common names
    """
    return df.loc[(df['Common Names'].str.contans(r'\Bear\b',
                                                  flags=re.IGNORECASE)) &
                  df["Category"] == "Mammal", "Park Name"]





def main():

    df_species = pd.read_csv('species.csv', index_col=1, usecols=range(13))
    df_parks = pd.read_csv('parks.csv', index_col=1)
    df_both = pd.merge(df_parks,df_species,on="Parl Name")
    df_both.set_index('State',inplace=True)

    # Question 1


    print(q1(df_species))

    # Question 2
    print(q2(df_species))

    # Question 3
    print(q3(df_species))
    # Question 4
    print(q4(df_species))
    # Question 5
    print(q5(df_species))
    # Question 6
    # print(q6(df_species))
    print(q7(df_species))



if __name__ == "__main__":
    main()
