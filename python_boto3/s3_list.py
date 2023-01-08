import boto3

# Create an S3 client
s3 = boto3.client('s3')

# List the objects in the bucket, list_objects_v2
response = s3.list_objects_v2(Bucket='sendtest2023')

# Print the object keys
for object in response['Contents']:
    print(object['Key'])
