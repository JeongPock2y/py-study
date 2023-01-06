import boto3

client = boto3.client('s3')
response = client.put_object(
    Bucket='sendtest2023',
    Key='hello.txt'

)