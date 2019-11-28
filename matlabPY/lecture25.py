# ----------------------------------------------------------------------
# Name:        lecture25
# Purpose:     Demonstrate the functionality of matploblib
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Skeleton module to be used in lecture 25.

Use matplotlib to explore and visualize the following datasets:
pypl.csv: PYPL PopularitY of Programming Language
          http://pypl.github.io/PYPL.html
iris.csv: iris flower dataset
top30.csv: top 30 most listened songs in the world by spotify
"""
import pandas as pd
import matplotlib.pyplot as plt
# Uncomment import below for 3-d demo only
# from mpl_toolkits import mplot3d


def explore_pypl():
    """
    Use matplotlib to explore the PYPL dataset
    """
    # Read the pypl csv file and use the language name as the index
    df_lang = pd.read_csv('PYPL.csv', index_col=1)
    top_lang = df_lang.loc["Python":"R","Share"]
    plt.bar(top_lang.index,top_lang,color="cmgrby")
    plt.xlabel("7 Most popular programming languages")
    plt.title("PYPL POP OF PRO LANG")
    plt.ylabel("Share")
    plt.show()



def explore_top30():
    """
    Use matplotlib to explore the PYPL dataset
    """
    # Read the top30 csv file and use song rank as index
    df_songs = pd.read_csv('top30.csv', index_col=0)
    plt.plot(df_songs["Length"])
    plt.xlabel("Song Rank")
    plt.ylabel("Length in seconds")
    plt.show()



def explore_iris():
    """
    Use matplotlib to explore the iris dataset
    """
    # Read the iris csv file and use the song rank as the index
    df_flowers = pd.read_csv('iris.csv', index_col=4)
    # Your code here



def main():
    # Uncomment one statement at a time to explore corresponding dataset
    explore_pypl()
    explore_top30()
    # explore_iris()

if __name__ == "__main__":
    main()
