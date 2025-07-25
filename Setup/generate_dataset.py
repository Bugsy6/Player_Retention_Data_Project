import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

num_players = 2000
players = [f'player_{i}' for i in range(1, num_players + 1)]

platforms = ['PC', 'Xbox', 'PS5']
regions = ['EU', 'NA', 'Asia']
bool_values = [True, False]

session_data = []
session_id_counter = 1

for player_id in players:
    num_sessions = np.random.randint(1, 10)
    signup_days_ago = np.random.randint(1, 60)
    signup_date = datetime.now() - timedelta(days=signup_days_ago)
    churned = random.choice(bool_values)
    
    for _ in range(num_sessions):
        days_since_signup = (datetime.now() - signup_date).days
        session_start = signup_date + timedelta(days=np.random.randint(0, days_since_signup),
                                                hours=np.random.randint(0, 24),
                                                minutes=np.random.randint(0, 60))
        session_duration_minutes = np.random.randint(5, 180)
        session_end = session_start + timedelta(minutes=session_duration_minutes)
        
        platform = random.choice(platforms)
        region = random.choice(regions)
        kills = np.random.poisson(10)
        deaths = np.random.poisson(3)
        level = np.random.randint(1, 51)
        is_premium = random.choices([True, False], weights=[0.3, 0.7])[0]
        made_purchase = is_premium and random.choices([True, False], weights=[0.5, 0.5])[0]
        
        session_data.append([
            player_id,
            f'session_{session_id_counter}',
            session_start,
            session_end,
            platform,
            region,
            kills,
            deaths,
            level,
            is_premium,
            made_purchase,
            days_since_signup,
            churned
        ])
        
        session_id_counter += 1

columns = ['player_id', 'session_id', 'session_start', 'session_end', 'platform', 'region',
           'kills', 'deaths', 'level', 'is_premium_user', 'made_purchase', 'days_since_signup', 'churned']

df = pd.DataFrame(session_data, columns=columns)
df.to_csv("fake_game_sessions.csv", index=False)
