import boto3

aws_connection = boto3.session.Session(profile_name="profile_name")
cloudwatch = aws_connection.client('logs')

log_group_to_scan="/aws/lambda/YourLambdaName"
log_stream_filter_prefix="2022/05/07/"

try:

    response = cloudwatch.describe_log_streams(logGroupName=log_group_to_scan, descending=True,
                                                logStreamNamePrefix=log_stream_filter_prefix)

    for logstream in response["logStreams"]:

        logstream_name = logstream["logStreamName"]
        print(f"Extracting logs for stream {logstream_name}")

        log_details = cloudwatch.get_log_events(
            logGroupName=log_group_to_scan,
            logStreamName=logstream_name,
        )

        for event in log_details["events"]:
            timestamp = int(event["timestamp"])
            message = str(event["message"])

            print(f"{timestamp}:{message}")

except Exception as e:
	print(e)
