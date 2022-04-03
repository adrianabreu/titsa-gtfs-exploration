import pandas as pd
def fix_gtfs_time(df: pd.DataFrame, cols: [str], curr_date: str)-> pd.DataFrame: 
    '''
    This method converts the problematic gtfs format (which goes from 00:00:00 to 27:00:00) into a valid date time format
    It will append the time to the current date applying the extra hours to the next day.
    For example for the following row:
    
    |r | a |  b |
    | -- | -- | -- |
    | 1 | 23:50:00 | 24:15:00 |

    And the date 2022-03-15, it will yield:

     |r | a |  b |
    | -- | -- | -- |
    | 1 | 2022-03-15 23:50:00 | 2022-03-16 00:15:00 |   

    ''' 
    for col_name in cols:
        df[col_name + "_day"] = 0
        mask = df[col_name] > '23:59:59'
        df.loc[mask,col_name + "_day"] = 1
        df[col_name] = df[col_name].apply(lambda x: f'{curr_date} {(int(x.split(":")[0])-24):02d}{x[x.find(":"):]}' if x > '23:59:59' else f'{curr_date} {x}')
        df[col_name] = pd.to_datetime(df[col_name]) + pd.to_timedelta(df[col_name + "_day"], unit='days')

        df = df.drop(col_name + "_day", axis=1)
    return df