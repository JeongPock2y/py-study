# deletetable.py
# https://cumulus.tistory.com/61
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')
table.delete()