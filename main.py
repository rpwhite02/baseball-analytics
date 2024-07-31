import streamlit as st
import pandas as pd
from scripts.batting_viz import hr_scatter, scatter_matrix
from scripts.pitching_viz import team_stat_starters

### EDIT TEXT USING MARKDOWN, STREAMLIT FORMATS LOOK LIKE SHIT

### KEEP RESEARCHING BETTER METHODS THIS FILE LOOKS LIKE SHIT

def home():
    st.title("Analyzing Baseball Trends and Insights")
    st.write("""
    ## Introduction
    This project provides an in-depth analysis of baseball statistics, including interactive visualizations and machine learning predictions
    to derive meaningful insights. I use batting, pitching, and fielding data from the 2012 season that can be found
    [here](https://www.kaggle.com/datasets/open-source-sports/baseball-databank/data?select=Teams.csv)
    
    ### Pages
    
    #### Batting Analysis

    - **Interactive Charts**: Visualize offensive stats such as batting average, OPS, hone runs, etc.
    - **Player Analysis**: Focus on individual player performance and trends over time.
    - **Advanced Metrics**: Gain insights into advanced batting metrics and their implications.
             
    #### Pitching Analysis
             
    - **Key Statistics**: Examine pitching stats like ERA, strikeout rates, and WHIP.
    - **Team and Individual Performance**: Analyze how different teams perform on the mound.
    - **Comparative Analysis**: Compare pitchers across various metrics to identify top performers.
    """)
    

def batting():
    # Talk about the data a little bit, such as year, how things were calculated, etc.

    batters = pd.read_csv('data/2012_csvs/2012_Batters.csv')
    top10_hr = batters.nlargest(10, 'HR')

    st.header('Batting Data Table')
    st.write(batters)

    st.header('Scatter Matrix of Batting Average and Fielding Percentage of Players in 2012')
    scatter_matrix(batters)

    # Talk about correlations between the scatter plots

    st.header('Top 10 Homerun Hitters in 2012 and Their Offensive Stats')
    hr_scatter(top10_hr)

    # Talk about the different batters listed, how homerun count can correlate with other offensive stats

def pitching():
    # Talk about the data a little bit, such as year, how things were calculated, etc.

    starters = pd.read_csv('data/2012_csvs/2012_Starters.csv')

    st.header('Team Pitching Stats')
    team_stat_starters(starters)

    # Talk about correlations between different team pitching stats, compare them to real life like how many runs
    # each team gave up during the season, Remember to distinguish that it's all starting pitchers so that could lead to findings
    # like a signal of a weak bullpen.

### def fielding(): FIELDING DATA NOT SURE WHAT TO DISPLAY YET

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", ["Home", "Batting Analysis", "Pitching Analysis"])

    if selection == "Home":
        home()
    elif selection == "Batting Analysis":
        batting()
    elif selection == "Pitching Analysis":
        pitching()

if __name__ == "__main__":
    main()