# s3_download.py

import boto3

s3 = boto3.client('s3')
s3.download_file('boto3-ywj-bucket', 'pic.png', 'pic2.png')