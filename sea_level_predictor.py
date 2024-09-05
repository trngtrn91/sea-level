import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    fig, ax = plt.subplots()

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
    


    # Create first line of best fit
    years_extended = pd.Series(range(1880, 2051, 1))
    line1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    line2 = [line1.slope*xi + line1.intercept for xi in years_extended]

    plt.plot(years_extended, line2)


    # Create second line of best fit
    years_extended2 = pd.Series(range(2000, 2051, 1))
    line3 = linregress(df[df["Year"] >= 2000]["Year"], df[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"])
    line4 = [line3.slope*xi + line3.intercept for xi in years_extended2]

    plt.plot(years_extended2, line4)


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()