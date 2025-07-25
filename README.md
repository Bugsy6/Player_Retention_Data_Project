# Introduction
Welcome to my analysis of player session data, focusing on player churn and retention. This projects purpose was to help identify the factors that affect player retention and to identify any clear patterns that lead to player churn over a 7, 14 and 30 day period.

My data was generated via a [Dataset Generate](/Setup/generate_dataset.py) Python script included in the Setup folder. The script generated thousands of players and sessions, with related details such as platform, session start and end time, sign up date, gameplay details, and premium user indicators. Through Python scripts I explored the potential patterns and factors that contribute to a player's retention. 

# Project Goals
I began by identifying a few potential factors that may contribute to player churn. Initially looking for general patterns and then to go on to dig further into factors around premium users and purchases.

## Initial Goals
1. What is the average session length by platform?
2. What % of players churn within 7 / 14 / 30 days?
3. How does churn differ by platform or region?

## Further Goals
1. Are premium users more likely to be retained?
2. Are purchases predictive of retention?

# Tools Used
I used several tools during this project.

- Python
    - Pandas Library: Data Cleaning, Processing and Analysing.
    - Matplotlib: Used to visualise the data.
- Jupyter Notebooks: A great tool to both run the analysis and report on the results.
- Visual Studio Code: Main development environment
- Git & GitHub: Used to version control and share my project. 

# Analysis
## Data Import
The data was imported from the generated CSV into a Dataframe with Pandas.

## Data Cleaning
An intial clean up was done on the data. Checking for empty, missing or NaN data, and finally removing duplicates.

The *session_start* and *session_end* fields were converted to DateTime objects for consistancy and more efficient analysis.

## Session Duration Analysis
I did some initial analysis on the session duration by adding a new *session_duration* column and then running the describe function to see some headline details.

```python
# Adding session duration field
df['session_duration'] = (df.session_end - df.session_start) / pd.Timedelta(minutes=1)
median_duration = df.session_duration.mean()

df.session_duration.describe()
```

I then broke this down further by Region.

![Session Duration by Region](/Images/duration_region.png)

And then by Platform, finding a similar result across all.

![Session Duration by Platform](/Images/duration_platform.png)

## Retention Analysis
I then went on to look at retention across 7, 14 and 30 day periods. 

```python
churn_7days = df.groupby('player_id')['days_since_signup'].max().between(1, 7).sum()
churn_14days = df.groupby('player_id')['days_since_signup'].max().between(8, 14).sum()
churn_30days = df.groupby('player_id')['days_since_signup'].max().between(15, 30).sum()

total_players = df.player_id.nunique()

retention_7days = ( churn_7days / total_players ) * 100
retention_14days = ( churn_14days / total_players ) * 100
retention_30days = ( churn_30days / total_players ) * 100
```

I then visualised this as a table.

![Retention over 7, 14 and 30 days](/Images/retention_days.png)

I then continued to slice this data further by platform.

```python
thresholds = [7, 14, 30]
platform_churn = {}

for platform in ['PC', 'PS5', 'Xbox']:
    subset = last_played[last_played['platform'] == platform]
    platform_churn[platform] = {}

    for t in thresholds:
        churned = subset[subset['days_since_signup'] <= t]
        platform_churn[platform][f'{t} days'] = len(churned)
        platform_churn[platform][f'{t} days %'] = (
            f'{len(churned) / len(subset):.1%}' if len(subset) > 0 else "N/A"
        )
```

Then plotted the results in a similar table for comparison.

![Retention over 7, 14 and 30 days by platform](/Images/retention_platform.png)

# What I learned

Through this project I deepen my knowledge of player retention and the factors that can contribute to it. I also enhanced my technical skills with Python and the Pandas library. A few key take aways:

- Power and efficiency of Python libraries: I gain a lot of new understanding about some of the more advanced features of the Pandas, Matplotlib, Numpy and DateTime libraries. These libraries can help to deliver complex tasks with great efficiency.
- Importance of Data Cleaning: We need to be sure of the validity and accuracy of the data before performing any analysis. Having anomalies, outliers and missing data can easily skew the results and give an entirely different insight.
- My Ability to Learn: I was really pleased with how I managed to pick up and learn some of these more advanced library functions. My ability to read and understand documentation as well as just to try things has really grown in this project.

# Insights

The analysis I performed seemed to suggest a few key factors toward player retention:

- Player's Region and Platform has no major impact on retention
- Retention seems to be mostly be a longterm issue with the majority of churn occurring after 14 days

This has lead me to believe that player's investment in the game (via premium payments or purchases) may be a larger contributing factor and I would like to investigate that further. Although there is also the potential that the gameplay itself is a big factor. Difficulty spikes, lack of end game content, repetitive gameplay and lack of postivie reward stimulus may all play a huge role in churn and potential a more widespread role.

# Challenges

I faced a few challenges while running this project, but I still believe this was a good learning opportunity:

- Lack of real world data: although my dataset was interesting and served its purpose it lacked the nuances, anomalies and erros of real world data. This meant I didn't get to practice as much data cleaning as I would have liked.
- Visualisation: I haven't used Matplotlib much prior to this project so did find it difficult to present data in the way I really wanted. I did find it very intiuitive to use through Pandas, but lacked the visual customisation I would have liked. I have looked at another library called Seaborn that may help with this.

Continuing on this project I would like to continue to research into better way to visualise the data, as well as looking at splitting the project up into separate Jupyter Notebooks for each goal of the project.

# Conclusion

This has been a really interesting and insightful project, it made me think more deeply about the factors that could affect a player's retention, and how it can come from not only from the gameplay but also the player's sense of investment in the game, whether that be monetary or social.

Working with Python and the Pandas library in particular has been a great experience. I look forward to exploring more of Pandas and seeing what further analysis I can find around premium users, monetary investments, and gameplay factors.