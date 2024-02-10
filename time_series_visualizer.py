import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

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


    # Draw bar plot
    # Sort the DataFrame by date
    df_bar = df_bar.sort_index()

    # Create figure and axis objects
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the bar chart
    ax.bar(df_bar.index, df_bar['value'], color='skyblue')

    # Set labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.set_title('Bar Plot')

    # Rotate x-axis labels for better readability (optional)
    plt.xticks(rotation=45)

    # Tight layout to prevent clipping of labels
    plt.tight_layout()


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
