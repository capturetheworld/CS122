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
    What states have the most species?
     """

    counts_by_state = df["Common Names"].groupby("State").count()

    print(counts_by_state)
    return(counts_by_state.idxmax())


def q2(df):
    """
    What states have the most endangered/proposed endangered species?
    BOOLEAN MASK + WITH GROUPBY
     """
    endangered = df.loc[df["Conservation Status"].str.contains(
        "Endangered",na=False),
                     "Common Names"].groupby("State").count()

    return(endangered.idxmax())

# def q3(df):
#     """
#    Multilevel indexing
#      """
#     endangered = df.loc[df["Conservation Status"].str.contains(
#         "Endangered",na=False),
#                      "Common Names"].groupby("State").count()
#
#     return(endangered.idxmax())


def main():

    df_species = pd.read_csv('species.csv', index_col=1, usecols=range(13))
    df_parks = pd.read_csv('parks.csv', index_col=1)
    df_both = pd.merge(df_parks,df_species,on="Park Name")
    df_both.set_index('State',inplace=True)
    print(df_both.head())

    # Question 1


    print(q1(df_both))
    print(q2(df_both))
    print(q3(df_both))
    # print(q4(df_both))
    # print(q5(df_both))
    # print(q6(df_both))
    # print(q7(df_both))








if __name__ == "__main__":
    main()
