import pandas as pd
import calendar
import datetime as dt
from gymbook import utilities as utils

def read_logs(csv: str) -> pd.DataFrame:
    """
    Read in workout logs output from Gymbook mobile app
    
    :param csv: The .csv file containing workout logs from the Gymbook
        mobile application.
        
    :return: Dataframe in raw form but cleaned
    """
    df = pd.read_csv(
        csv,
        sep=",",
        encoding = "utf-8"
    )
    
    # Obtain list of columns
    unsplit_columns = list(df.columns)[0]
    columns = unsplit_columns.split(',')
    
    # Split out the 1 column to many
    df[columns] = df['Date,Workout,Time,Exercise,Region,Muscle Group (Primary),Muscle Group (Secondary),Repetitions / Time,Weight / Distance,Notes,Skipped'].str.split(',', expand=True)
    
    # Drop the old ridiculous column
    df = df.drop(columns=['Date,Workout,Time,Exercise,Region,Muscle Group (Primary),Muscle Group (Secondary),Repetitions / Time,Weight / Distance,Notes,Skipped'])
    
    # Additional columns
    df['Date'] = pd.to_datetime(df['Date'])
    df['dayofweekidx'] = df['Date'].dt.dayofweek

    df['dayofweek'] = df['dayofweekidx'].apply(lambda x: calendar.day_name[x])
    df.head()

    df['Timefloat'] = pd.to_datetime(df['Time'])
    df['Timefloat'] = df['Timefloat'].dt.hour + df['Timefloat'].dt.minute / 60.0
    
    df['Weight / Distance'] = df['Weight / Distance'].apply(utils.convert_kg_to_float)
    df['Repetitions / Time'] = df['Repetitions / Time'].apply(utils.convert_reps_to_int)
    df['Weight Lifted'] = df['Repetitions / Time'] * df['Weight / Distance']
    
    return df


def aggregate_exercises(df):
    """
    
    """
    agg_exercises = df.groupby(['Date', 'Exercise'], as_index=False).sum()
    
    agg_exercises = (agg_exercises.drop(columns=['dayofweekidx', 'Timefloat'])
     .rename({
         'Repetitions / Time' : 'Repetitions',
         'Weight / Distance' : 'Weight',
     }))
    
    agg_exercises['Number Average Rep Weight'] = agg_exercises['Weight Lifted'] / agg_exercises['Repetitions / Time']
    
    return agg_exercises