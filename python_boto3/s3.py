import boto3

client = boto3.client('s3')
response = client.put_object(
    Bucket='receive2023',
    Key='/hello'

)