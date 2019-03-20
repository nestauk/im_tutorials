import ast
import smart_open

def eval_cols(cols):
    '''eval_cols
    Returns a dictionary to convert columns with ast.literal_eval when reading
    a csv with pandas.

    Args:
        cols (`list` of `str`): List of column names

    Returns:
        (`dict`): Dict of column name keys and ast.literal eval as values
    '''
    return {col: ast.literal_eval for col in cols}

def gateway_to_research_projects():
    '''gateway_to_research_projects
    Get Gateway to Research projects csv and return as dataframe.
    '''
    bucket='innovation-mapping-tutorials'
    gtr_projects_key='gateway-to-research/gtr_projects.csv'
    list_cols = ['research_topics', 'research_subjects']
    gtr_projects_df = pd.read_csv(
        smart_open.smart_open(f'https://s3.us-east-2.amazonaws.com/{bucket}/{gtr_projects_key}'),
        converters=eval_cols(list_cols),
        index_col=0
    )
    return gtr_projects_df
