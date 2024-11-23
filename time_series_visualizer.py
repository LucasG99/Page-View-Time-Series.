import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

# Draw line plot
def draw_line_plot():
    # Create the figure and plot the line chart
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['value'], color='r', linewidth=1)
    
    # Add labels and title
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    
    # Save and return the figure
    fig.savefig("line_plot.png")
    return fig

# Draw bar plot
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Plot the bar chart
    fig = df_bar.plot(kind='bar', figsize=(12, 6), legend=True).figure
    
    # Add labels and title
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                                       "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    
    # Save and return the figure
    fig.savefig("bar_plot.png")
    return fig

# Draw box plot
def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.month
    df_box['month_name'] = df_box['date'].dt.strftime('%b')
    df_box['month_name'] = pd.Categorical(df_box['month_name'], categories=["Jan", "Feb", "Mar", "Apr", 
                                                                            "May", "Jun", "Jul", "Aug", 
                                                                            "Sep", "Oct", "Nov", "Dec"], 
                                          ordered=True)

    # Ensure the value column is of type float
    df_box['value'] = df_box['value'].astype(float)

    # Create the box plots
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Year-wise Box Plot
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    
    # Month-wise Box Plot
    sns.boxplot(x='month_name', y='value', data=df_box, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    
    # Save and return the figure
    fig.savefig("box_plot.png")
    return fig
