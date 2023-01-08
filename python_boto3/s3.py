import boto3

client = boto3.client('s3')
client = boto3.client('cloudwath')
response = client.put_object(
    Bucket='sendtest2023',
    Key='hello.txt'

)
response = client.list_buckets() # bucket 목록
print(response)


