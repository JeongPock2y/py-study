import boto3
#https://aws.amazon.com/ko/premiumsupport/knowledge-center/cloudwatch-getmetricdata-api/
# Create a CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# Set the region
region = 'ap-northeast-2'

# Set the namespace for EC2 metrics
namespace = 'AWS/EC2'

# Set the metric name
metric_name = 'CPUUtilization'

# Set the dimensions for filtering the results
dimensions = [{
    'Name': 'InstanceId',
    'Value': 'i-016e4006e19c68bde'
}]

# Set the start and end times for the data to be retrieved
start_time = '2023-01-07T00:00:00Z'
end_time = '2023-01-07T01:00:00Z'

# Set the period to 1 hour (3600 seconds
period = 600

# Set the statistic to retrieve the average value
statistic = 'Average'

# Retrieve the metric data 메트릭 통계
metric_data = cloudwatch.get_metric_statistics(
    Namespace=namespace,
    MetricName=metric_name,
    Dimensions=dimensions,
    StartTime=start_time,
    EndTime=end_time,
    Period=period,
    Statistics=[statistic]
)

# Print the metric data
print(metric_data)

# This code will retrieve the average CPU utilization for the specified EC2 instance over the specified time period 
# (in this case, one day). 
# You can customize the code to retrieve data for other time periods, 
# instances,or metrics by changing the relevant parameters.