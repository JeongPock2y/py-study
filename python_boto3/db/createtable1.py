# createtable.py

import boto3

# - 테이블(Table)

# - 항목(Items)

# - 속성(Attributes)

# - 기본키
#
# S - the attribute is of type String
# N - the attribute is of type Number
# B - the attribute is of type Binary

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='users')

# Print out some data about the table.
print(table.item_count)





#이미존재하는 테이블 사용
# import boto3
# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('users')


