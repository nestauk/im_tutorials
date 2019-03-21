import smart_open
import pandas as pd
import ast

S3_PATH = f'https://s3.us-east-2.amazonaws.com/innovation-mapping-tutorials/{key}'

def _projects_h2020_fp7(key):
    df = pd.read_csv(
    smart_open(S3_PATH)
    sep=';',
    encoding='iso-8859-1',
    parse_dates=['startDate', 'endDate'],
    infer_datetime_format=True,
    decimal=','
    )
    df['participants'] = df['participants'].str.split(';')
    df['participantCountries'] = df['participantCountries'].str.split(';')
    df['startYear'] = df['startDate'].dt.year
    df['endYear'] = df['endDate'].dt.year
    df['organisations'] = (df['coordinator'] + ';' +  df['participants']).fillna(df['coordinator'])
    df['countries'] = (df['coordinatorCountry'] + ';' +  df['participantCountries']).fillna(df['coordinatorCountry'])
    return df


def h2020_projects():
    key = 'cordis/h2020/cordis-h2020projects.csv'
    return _projects_h2020_fp7(key)

def fp7_projects():
    key = 'cordis/h2020/cordis-fp7projects.csv'
    return _projects_h2020_fp7(key)
