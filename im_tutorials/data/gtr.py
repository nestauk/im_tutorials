import ast
import smart_open
import pandas as pd

from im_tutorials.utilities import eval_cols 
from im_tutorials.data.s3_transfer import load_df_pkl

bucket = 'innovation-mapping-tutorials'
folder = 'gtr'

def gtr_sample():
    '''gateway_to_research_projects
    Get Gateway to Research projects csv and return as dataframe.
    '''
    bucket='innovation-mapping-tutorials'
    gtr_projects_key='gateway-to-research/gtr_projects.csv'
    list_cols = ['research_topics', 'research_subjects']
    gtr_projects_df = pd.read_csv(
        smart_open.smart_open("https://s3.us-east-2.amazonaws.com/{}/{}".format(bucket, gtr_projects_key)),
        converters=eval_cols(list_cols),
        index_col=0
    )
    return gtr_projects_df

def gtr_table(table):
    '''gtr_table
    Get a table from the Gateway to Research database.

    Parameters
    ----------
    table : str
        Name of the table to load. Tables available include:
            - funds
            - link_table
            - organisations
            - organisations_locations
            - outcomes_artisticandcreativeproducts
            - outcomes_collaborations
            - outcomes_disseminations
            - outcomes_furtherfundings
            - outcomes_impactsummaries
            - outcomes_intellectualproperties
            - outcomes_keyfindings
            - outcomes_policyinfluences
            - outcomes_products
            - outcomes_publications
            - outcomes_researchdatabaseandmodels
            - outcomes_researchmaterials
            - outcomes_softwareandtechnicalproducts
            - outcomes_spinouts
            - participant
            - persons
            - projects
            - topic
    Returns
    -------
    DataFrame
        A dataframe with containing the GtR table data.
    '''
    key=f'{folder}/gtr_{table}.pkl.bz2'
    return load_df_pkl(bucket, key)

def gtr_table_list():
    d = [
            'funds',
            'link_table',
            'organisations',
            'organisations_locations',
            'outcomes_artisticandcreativeproducts',
            'outcomes_collaborations',
            'outcomes_disseminations',
            'outcomes_furtherfundings',
            'outcomes_impactsummaries',
            'outcomes_intellectualproperties',
            'outcomes_keyfindings',
            'outcomes_policyinfluences',
            'outcomes_products',
            'outcomes_publications',
            'outcomes_researchdatabaseandmodels',
            'outcomes_researchmaterials',
            'outcomes_softwareandtechnicalproducts',
            'outcomes_spinouts',
            'participant',
            'persons',
            'projects',
            'topic',
        ]
    return d
