import os
import datetime
import boto3


# 파일이 저장되어 있는 디렉토리 지정
directory = "/Users/choongmankim/Git Repo/Python/test/pressure"

## 현재 시간에서 1시간 과거를 기준시간으로 지정
destTime = datetime.datetime.now() - datetime.timedelta(hours=1)


destDay = destTime.strftime("%Y" + "-" + "%m" + "-" + "%d")

destHour = destTime.strftime("%H")

# 파일명 생성
# file_name = join('_', ["pressure", "2023-01-03", "04"]) + ".tsv"
test_list = ["pressure", destDay, destHour]
file_name = "_".join(test_list) + ".tsv"

# print(destHour)
# 파일명 맞는지 출력
print(file_name)

## Boto3 S3 파일 전송부분
# 클라이언트 선언
s3_client = boto3.client("s3")

# 파일명 지정
# file_name = srcDir + file[3] + ".mp3"

## 버킷내부에서 어떤 디렉토리에 어떤 파일명으로 저장될지 지정함
object_name = "_".join([str(file[0]), str(file[2]), str(file[3])]) + ".tsv"

# S3 Upload
response = s3_client.upload_file(file_name, s3_bucket, object_name)