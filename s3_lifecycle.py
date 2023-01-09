from http import client
import boto3
from datetime import datetime, timedelta

s3 = boto3.resource('s3')
s3 = boto3.client('s3')

#bucket_name = 'sendtest2023'

#bucket_lifecycle = s3.BucketLifecycle('bucket_name')
#bucket_lifecycle_configuration = s3.BucketLifecycleConfiguration('bucket_name')

response = client.put_bucket_lifecycle_configuration(
    Bucket='sendtest2023',
    ChecksumAlgorithm='SHA256',
    LifecycleConfiguration={
        'Rules': [
            {
                'Expiration': {
                    'Date': datetime(2023, 1, 12),
                    'Days': 3,
                    'ExpiredObjectDeleteMarker': True
                },
                'ID': 'string',
                'Prefix': 'string',
                'Filter': {
                    'Prefix': 'string',
                    'Tag': {
                        'Key': 'string',
                        'Value': 'string'
                    },
                    'ObjectSizeGreaterThan': 123,
                    'ObjectSizeLessThan': 123,
                    'And': {
                        'Prefix': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'ObjectSizeGreaterThan': 123,
                        'ObjectSizeLessThan': 123
                    }
                },
                'Status': 'Enabled'|'Disabled',
                'Transitions': [
                    {
                        'Date': datetime(2023, 10, 1),
                        'Days': 123,
                        'StorageClass': 'STANDARD_IA'
                    },
                ]
            }
        ]
    },
    ExpectedBucketOwner='string'
)