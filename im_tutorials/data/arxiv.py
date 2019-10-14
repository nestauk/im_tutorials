import ast
import smart_open
import pandas as pd

from im_tutorials.utilities import eval_cols, double_eval


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
