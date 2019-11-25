# ----------------------------------------------------------------------
# Name:        lecture24
# Purpose:     Demonstrate the use of Pandas
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Skeleton module to be used in lecture 24.

Demonstrate using Pandas to answer the following questions about
National Parks.
What state is Glacier National Park in?
What is the park code and acreage of Yosemite National Park?
What is the largest national park in the US?
What state is home to the smallest national park?
How many national parks are there in Washington State?
How many national parks are there in California?
What is the average acreage of National parks?
What is the total area occupied by national parks in each state and
between which latitudes/longitudes are these parks located?
"""
import pandas as pd
import numpy as np

def q1(df):
    """
    What state is Glacier National Park in?
    :param df: Pandas DataFrame representing the data in parks.csv
    :return: string - the name of the state where Glacier National Park
            is located
    """
    return df.loc['Glacier National Park', 'State']

def q2(df):
    """
    What is the park code and acreage of Yosemite National Park?
    :param df: Pandas DataFrame representing the data in parks.csv
    :return: tuple (string, integer) Park code and acreage
    """
    return (df.loc['Yosemite National Park', 'Park Code'],
            df.loc['Yosemite National Park', 'Acres'])

def q3(df):
    """
    What is the largest national park in the US?
    :param df: Pandas DataFrame representing the data in parks.csv
    :return: string - name of the largest park.
    """
    return df['Acres'].idxmax()

def q5(df):
    """
    What is the park code and acreage of Yosemite National Park?
    :param df: Pandas DataFrame representing the data in parks.csv
    :return: tuple (string, integer) Park code and acreage
    """
    # Your code here
    return len(df[df["State"]=='WA'])


def q6(df):
    """
    # of national parks in CA, but problem is Death Valley is in CA and NV
    """
    # Your code here
    return len(df[df['State'].str.contains('CA')])

def q7(df):
    """
    Average acreage of national parks
    """
    # Your code here
    return df['Acres'].mean()

def q8(df):
    """
    Sum the acrage and compute min and max of latitude and longitude
    """
    # Splits data frames
    # for group, dframe in df.groupby("State"):
    #     print(group,dframe)

    # Take the sum result = df.groupby("State").sum() - sums all columns


    return df.groupby("State").agg({"Acres":np.sum,"Latitude":(np.max,
                                                                   np.min),
                                        "Longitude":(np.max,np.min)})

def main():
    # Read the csv file and use column 1 (Park Name) as our index
    df_parks = pd.read_csv('parks.csv', index_col=1)

    # Question 1
    print(f'Glacier National Park is in {q1(df_parks)}.')

    # Question 2


    # Question 3


    # Question 4


    # Question 5
    print(q5(df_parks))


    # Question 6
    print(q6(df_parks))


    # Question 7
    print(q7(df_parks))


    # Question 8
    print(q8(df_parks))



if __name__ == "__main__":
    main()
