import ast
import smart_open
import pandas as pd

from im_tutorials.utilities import eval_cols 


def gateway_to_research_projects():
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
