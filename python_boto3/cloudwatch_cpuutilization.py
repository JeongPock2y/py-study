import boto3
from datetime import datetime, timedelta

client = boto3.client('cloudwatch')

# Set the start and end times to the past 24 hours
start_time = datetime.utcnow() - timedelta(hours=1) + timedelta(hours=9)
end_time = datetime.utcnow() + timedelta(hours=9)
print(start_time)
print(end_time)

response = client.get_metric_statistics(
        Namespace='EC2',
        MetricName='CPUUtilization',
        Dimensions=[
            {
            'Name': 'InstanceId',
            'Value': 'i-016e4006e19c68bde'
            },
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=600,
        Statistics=[
            'Average',
        ],
        Unit='Percent'
    )

for cpu in response['Datapoints']:
    if 'Average' in cpu:
        print(cpu['Average'])
#print(cpu)
print("cloudwatch metrics3")
