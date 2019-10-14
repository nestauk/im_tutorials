import smart_open
import pandas as pd
import pickle

from im_tutorials.data.s3_transfer import load_df_pkl


def patents_10k():
    '''patents_10k
    Gets a pre-selected sample of 10,000 patents from ONS.
    '''
    bucket='innovation-mapping-tutorials'
    patents_10k_key='ons/ONS_y02_sample_10000.pkl.bz2'
    return load_df_pkl(bucket, patents_10k_key)

def patents_100k():
    '''patents_100k
    Gets a pre-selected sample of 100,000 patents from ONS.
    '''
    bucket='innovation-mapping-tutorials'
    patents_100k_key='ons/ONS_y02_sample_100000.pkl.bz2'
    return load_df_pkl(bucket, patents_100k_key)
