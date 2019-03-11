import boto3
import io

def download_file_s3(client, bucket, file):
    '''download_file_s3
    Downloads a file from S3 and reads it.

    Args:
        client (:obj:`boto3.s3_client`): An S3 client
        bucket (str): S3 bucket
        file (:obj: `boto3.file_obj`): S3 file object

    Returns:
        (:obj:`io.BytesIO`): File object
    '''
    obj = client.get_object(Bucket=bucket, Key=file['Key'])
    return io.BytesIO(obj['Body'].read())

def get_files_from_s3(bucket, folder, key_prefix=''):
    '''get_files_from_s3
    Gets multiple files from S3 given a bucket, folder and file prefix.

    Args:
        bucket (str): S3 bucket
        folder (str): S3 folder
        key_prefix (str): S3 file name prefix
    '''
    s3_client = boto3.client('s3')
    response = s3_client.list_objects(
        Bucket=bucket,
        Delimiter='/',
        Prefix='/'.join([folder, key_prefix])
    )
    files = response['Contents']
    for file in files:
        yield download_file_s3(s3_client, bucket, file)
