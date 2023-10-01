"""
Author: ALine Lemos de Freitas
Created at 01/10/2023

The idea of this code is to count the number of days you have already been
to a country and how many days you are autorized to stay as a tourist
considering the limit of 90 days in a rowling window of 180 days
"""

import pandas as pd
from datetime import datetime, timedelta

# Starting a new dataframe with 180 days from today
# Get today's date
today = datetime.today().strftime('%Y-%m-%d')
# future_date = today + timedelta(days=180)

# Generate a date range going back 180 days
date_range = pd.date_range(end=today, periods=180, freq='D')

# Create a DataFrame with the date range and set 'Date' column as the index
df = pd.DataFrame(index=date_range)

# Add a single column of zeros
df['InContry'] = 0


# adding the days when I was there
df['2023-07-20':'2023-07-30'] = 1
df['2023-08-05':'2023-09-01'] = 1
df['2023-09-04':'2023-09-25'] = 1

# Save this df as a pickle
df.to_pickle('calendar.pkl')

# Print the DataFrame
print(df)


# first day I was there on the last 180 days:
first_day = df.loc[df['InContry'] == 1].index[0].strftime('%Y-%m-%d')

# count 180 days from there
last_day_window = pd.date_range(start=first_day,
                                periods=180,
                                freq='D')

# this window will last until:
last_day = last_day_window[-1]
print(f"You have {90 - df['InContry'].sum()} days left\
      on a window that will last until\
      {last_day.strftime('%Y-%m-%d')}")
