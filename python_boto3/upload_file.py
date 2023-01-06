# boto3 Docs
import boto3
s3 = boto3.resource('s3')
#Filename, Bucket, Key  [Filename에 있는 파일을 sendtest2023버킷에  hihi.txt라는이름으로 업로드]
s3.meta.client.upload_file("C:\\Users\\dusdn\\py-study\\python_boto3\\test_edit.py", 'sendtest2023', 'hihi.txt')