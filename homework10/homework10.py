# ----------------------------------------------------------------------
# Name:        homework10
# Purpose:     Fuel Economy Data
#
# Author:      Ian SooHoo
# ----------------------------------------------------------------------
"""
This Python program will answer the following questions:

How many cars are made by the division Acura? The function must return an integer.
How many 'Guzzlers'  (as indicated by the column 'Guzzler?')  are made by the manufacturer General Motors?
    The function must return an integer.
What is the value of the lowest combined Fuel Efficiency as given by "Comb FE (Guide) - Conventional Fuel"?
    The function must return a float.
What car line has the highest Highway FE - Conventional Fuel as given by "Hwy FE (Guide) -
    Conventional Fuel"? The function must return a string.
What is the average combined FE - Conventional Fuel among all wheel drives.  Use 'Drive Desc'.  The function must return a float.
Which car line has the largest difference between Highway and City Fuel efficiency - Conventional Fuel?  The function must return a string.
What is the average annual fuel cost (Annual Fuel1 Cost - Conventional Fuel) of supercharged cars?  Use the "Air Aspiration Method Desc"
    to identify  supercharged cars. The function must return a float.
What SUV has the highest annual fuel cost?   Use "Carline Class Desc" to identify SUVs.  The function must return the carline (a string).
Which manufacturer has the most cars with manual transmission?  The function must return a string.
What is the average annual fuel cost by car division?  The function must return a Pandas series.
What criteria would you use to buy a car?
    Each team member will write a function that returns their perfect car based on their own criteria.
    This function must return a string representing the perfect carline for you.  Please list your criteria clearly in the function docstring.
    Please include your name in the function name (for example q11_rula).
"""
import pandas as pd
import numpy as np


def q1(df):
    """
    How many cars are made by the division Acura?
    :param df: Pandas DataFrame representing the data in 2019 FE Guide.csv
    :return: integer - # of cars by division Acura
            is located
    """
    return len(df[df["Division"] == 'Acura'])


def q2(df):
    """
    How many 'Guzzlers'  (as indicated by the column 'Guzzler?')  are made by the manufacturer General Motors?
    The function must return an integer.
    :param df: Pandas DataFrame representing the data in 2019 FE Guide.csv
    :return: integer - Guzzlers are by GM

    """
    return len(df[(df["Guzzler?"] == ('G')) & (df["Mfr Name"] == "General Motors")])


def q3(df):
    """
    What is the value of the lowest combined Fuel Efficiency as given by "Comb FE (Guide) - Conventional Fuel"?
    :param df: Pandas DataFrame representing the data in 2019 FE Guide.csv
    :return: float - Lowest combined FE

    """
    return df["Comb FE (Guide) - Conventional Fuel"].min()


def q4(df):
    """
    What car line has the highest Highway FE - Conventional Fuel as given by "Hwy FE (Guide) -
    Conventional Fuel"?
    :param df: Pandas DataFrame representing the data in 2019 FE Guide.csv
    :return: string - highest Highway FE

    """
    return df["Hwy FE (Guide) - Conventional Fuel"].idxmax()


def q5(df):
    """
   What is the average combined FE - Conventional Fuel among all wheel drives.  Use 'Drive Desc'.
   The function must return a float.

    :param df: Pandas DataFrame representing the data in 2019 FE Guide.csv
    :return: float - average combined FE

    """
    return df.loc[df["Drive Desc"] == "All Wheel Drive", "Comb FE (Guide) - Conventional Fuel"].mean()


def q6(df):
    """
   Which car line has the largest difference between Highway and City Fuel efficiency - Conventional Fuel?
    The function must return a string.

    :param df: Pandas DataFrame representing the data in 2019 FE Guide.csv
    :return: string - car line with the largest difference Conventional Fuel

    """
    return (df["Hwy FE (Guide) - Conventional Fuel"] - df["City FE (Guide) - Conventional Fuel"]).idxmax()


def q7(df):
    """
   What is the average annual fuel cost (Annual Fuel1 Cost - Conventional Fuel) of supercharged cars?
   Use the "Air Aspiration Method Desc" to identify  supercharged cars. The function must return a float.

    :param df: Pandas DataFrame representing the data in 2019 FE Guide.csv
    :return: float - average annual fuel cost

    """
    return df.loc[(df['Air Aspiration Method Desc'] == 'Supercharged'), "Annual Fuel1 Cost - Conventional Fuel"].mean()


def q8(df):
    """
   What SUV has the highest annual fuel cost?   Use "Carline Class Desc" to identify SUVs.
   The function must return the carline (a string).
    :param df: Pandas DataFrame representing the data in 2019 FE Guide.csv
    :return: string - highest annual fuel cost

    """
    return df.loc[(df['Carline Class Desc'].str.contains('SUV', na=False)), "Annual Fuel1 Cost - Conventional Fuel"] \
        .idxmax()


def q9(df):
    """
   Which manufacturer has the most cars with manual transmission?  The function must return a string.
    :param df: Pandas DataFrame representing the data in 2019 FE Guide.csv
    :return: string - manufacturer that has the most cars with manual transmission

    """
    # return (df["Trans Desc"] == "Manual").groupby("Mfr Name").count()
    # return max_count.idxmax()

    manuals = df.loc[df["Trans Desc"] == "Manual"].groupby("Mfr Name").count()
    return manuals.index[0]


def q10(df):
    """
  What is the average annual fuel cost by car division?  The function must return a Pandas series.
    :param df: Pandas DataFrame representing the data in 2019 FE Guide.csv
    :return: Panda series - average annual fuel cost by car division

    """

    # return df["Annual Fuel1 Cost - Conventional Fuel"].mean().groupby("Division")

    average_fuel_df = df.groupby('Division').agg({"Annual Fuel1 Cost - Conventional Fuel": np.mean})
    return pd.Series(average_fuel_df['Annual Fuel1 Cost - Conventional Fuel'], index=average_fuel_df.index)



def q11_ian(df):
    """
  What criteria would you use to buy a car?
    Each team member will write a function that returns their perfect car based on their own criteria.
    This function must return a string representing the perfect carline for you.
    Please list your criteria clearly in the function docstring:

    Car needs to have 8 cylinders, be a turbocharged air aspirator, and have a semi-automatic transmission as I can't
    drive manual. I also want the highest HWY fuel efficiency from the resulting dataframe of the above conditions.
    Please include your name in the function name (for example q11_rula):

    :param df: Pandas DataFrame representing the data in 2019 FE Guide.csv
    :return: string - perfect carline

    """
    return df.loc[(df['# Cyl'] == 8) & (df['Air Aspiration Method Desc'] == "Turbocharged") & (df['Trans Desc'] ==
                                                                                               "Semi-Automatic"),
                  "Hwy Unadj FE - Conventional Fuel"].idxmax()


def main():
    # Read the csv file and use column Carline as our index, forget about Model since they are all 2019
    # df_fuel = pd.read_csv('2019 FE Guide.csv', index_col=1, usecols=range(13))
    df_fuel = pd.read_csv('2019 FE Guide.csv', index_col=2, usecols=range(1, 449))

    # print(df_fuel)
    # print(df_fuel.index.name)
    # Question 1
    print(q1(df_fuel))
    print(type(q1(df_fuel)))

    # Question 2
    print(q2(df_fuel))
    print(type(q2(df_fuel)))

    # Question 3
    print(q3(df_fuel))
    print(type(q3(df_fuel)))

    # Question 4
    print(q4(df_fuel))
    print(type(q4(df_fuel)))

    # Question 5
    print(q5(df_fuel))
    print(type(q5(df_fuel)))

    # Question 6
    print(q6(df_fuel))
    print(type(q6(df_fuel)))

    # Question 7
    print(q7(df_fuel))
    print(type(q7(df_fuel)))

    # Question 8
    print(q8(df_fuel))
    print(type(q8(df_fuel)))

    # Question 9
    print(q9(df_fuel))
    print(type(q9(df_fuel)))

    # Question 10
    print(q10(df_fuel))
    print(type(q10(df_fuel)))

    # Question 11
    print(q11_ian(df_fuel))
    print(type(q11_ian(df_fuel)))


if __name__ == "__main__":
    main()
