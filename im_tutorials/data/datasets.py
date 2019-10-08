import ast
import smart_open

import pandas as pd

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
        smart_open.smart_open("https://s3.us-east-2.amazonaws.com/{}/{}".format(bucket, gtr_projects_key)),
#         converters=eval_cols(list_cols),
        index_col=0
    )
    return gtr_projects_df

def sdg_web_articles():
    '''sdg_web_articles
    Get SDG web articles scraped from web and return as DataFrame.
    '''
    bucket='innovation-mapping-tutorials'
    gtr_projects_key='sdg/sdg_web_articles.json'
    list_cols = ['sdg_goals']
    gtr_projects_df = pd.read_json(
        smart_open.smart_open("https://s3.us-east-2.amazonaws.com/{}/{}".format(bucket, gtr_projects_key)),
        converters=eval_cols(list_cols),
        index_col=0
    )
    return gtr_projects_df

def double_eval(x):
    return ast.literal_eval(ast.literal_eval(x))

def arxiv_papers(year=2017):
    '''arxiv_papers
    Get arXiv papers csv for a single year and return as dataframe.

    Args:
        year (`int`): Year of the dataset.
    Returns:
        arxiv_df (`pd.DataFrame`): Parsed dataframe of arXiv papers.
    '''
    bucket='innovation-mapping-tutorials'
    key='arxiv_{}/arxiv_{}.csv'.format(year, year)
    arxiv_df = pd.read_csv(
        smart_open.smart_open('https://s3.us-east-2.amazonaws.com/{}/{}'.format(bucket, key)),
        index_col=0,
        converters={
            'authors': double_eval,
        },
        parse_dates=['created'],
    )
    arxiv_df['year_created'] = arxiv_df['created'].dt.year
    arxiv_df['category_ids'] = arxiv_df['category_ids'].str.split(',')
    return arxiv_df
