import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.all_buckets)
    print(bucket.name)
    
data =open(pic.jpg, 'rb')
s3.Bucket('test0126').put_object(Key='pic.jpg' , Body = data)


    
    