import pandas as pd
from smart_open import smart_open

S3_PATH = 'https://s3.us-east-2.amazonaws.com/innovation-mapping-tutorials/{}'

def country_basic_info():
    '''country_basic_info
    Country level data from RestCountries API.

    Fields:
       'alpha2Code', 'alpha3Code', 'altSpellings', 'area', 'borders',
       'callingCodes', 'capital', 'cioc', 'currencies', 'demonym', 'flag',
       'gini', 'languages', 'latlng', 'name', 'nativeName', 'numericCode',
       'population', 'region', 'regionalBlocs', 'subregion', 'timezones',
       'topLevelDomain', 'translations' 
    '''
    key = 'gis/countries_restcountries_api.json'
    df = pd.read_json(
            smart_open(S3_PATH.format(key))
            )
    df['lat'] = [l[0] for l in df['latlng']]
    df['lng'] = [l[1] for l in df['latlng']]
    return df
    
