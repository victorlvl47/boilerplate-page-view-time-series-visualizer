import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import numpy as np

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
top_quantile = df['value'].quantile(0.975)
bottom_quantile = df['value'].quantile(0.025)
cleaned_df = df[(df['value'] <= top_quantile) & (df['value'] >= bottom_quantile)]
df = cleaned_df


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(df.index, df['value'])

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar.index = pd.to_datetime(df_bar.index)

    # Group by year and month, and then calculate the mean
    monthly_average = df_bar.groupby([df_bar.index.year, df_bar.index.month]).mean()

    monthly_average.index = pd.to_datetime(monthly_average.index.map(lambda x: f'{x[0]}-{x[1]}'))

    # Extract unique years from the index
    unique_years = set(monthly_average.index.year)

    # Add columns for Year and Month
    monthly_average['Year'] = monthly_average.index.year
    monthly_average['Month'] = monthly_average.index.month

    # Pivot the dataframe
    pivot_df = monthly_average.pivot(index='Month', columns='Year', values='value')
    pivot_df.fillna(0, inplace=True)

    # set width of bar 
    barWidth = 0.06
    plt.subplots(figsize =(12, 8))

    # Set position of bars on X axis
    num_of_rows = len(pivot_df)
    offset = 0
    labels = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    hex_colors = [
        "#3366CC",  # January
        "#FF3366",  # February
        "#33CC33",  # March
        "#FF9900",  # April
        "#9933CC",  # May
        "#FFCC00",  # June
        "#6699FF",  # July
        "#FF6600",  # August
        "#0099CC",  # September
        "#FF3333",  # October
        "#99CC33",  # November
        "#FF6699"   # December
    ]
    for row in range(num_of_rows):
        bars = [x + offset for x in range(len(pivot_df.iloc[row]))] 
        offset += barWidth

        # Make the plot
        plt.bar(bars, pivot_df.iloc[row], color=hex_colors[row], width=barWidth, 
            edgecolor='black', label=labels[row]) 
    
    # Adding Xticks 
    plt.xlabel('Years', fontweight ='bold', fontsize = 15) 
    plt.ylabel('Average Page Views', fontweight ='bold', fontsize = 15) 
    plt.xticks([r + barWidth*6 for r in range(len(unique_years))], unique_years)
    
    plt.legend()

    fig = plt.gcf()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
