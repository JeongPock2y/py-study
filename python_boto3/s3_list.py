import boto3

# Create an S3 client
s3 = boto3.client('s3')
ec2 = boto3.client('ec2')
# List the objects in the bucket, list_objects_v2
response = s3.list_objects_v2(Bucket='sendtest2023')
response_key = ec2.describe_key_pairs()
#print(response_key['KeyPairs'])
for ob in response_key['KeyPairs']:
    a = (ob['KeyName'])
    
# Print the object keys
for object in response['Contents']:
    b = (object['Key'])
    print(object['Key'])

print(f'{a}')

