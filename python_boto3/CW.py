import boto3
import math
from datetime import datetime,timedelta

# Init variable
stage = 'prd'
cloudwatch = boto3.client('cloudwatch')
cluster_metrics = ['node_cpu_utilization', 'node_memory_utilization', 'cluster_node_count']
service_metrics = ['pod_cpu_utilization', 'pod_memory_utilization']


def get_service(metric):
    response = cloudwatch.list_metrics(
            Namespace='ContainerInsights',
            MetricName=metric,
            Dimensions=[
                    {
                        'Name':'ClusterName',
                        'Value':f'tah-{stage}-eks-cluster'
                    },
                    {
                        'Name':'Namespace',
                        'Value':'default'
                    },
                    {
                        'Name': 'Service'
                    }
                ]            
        )
    
    service = [metric['Value'] for metrics in response['Metrics'] for metric in metrics['Dimensions'] if metric['Name'] == 'Service']    
    return service

def get_service_metrics(time):
    for metric in service_metrics:
        service = get_service(metric)
        text = f"service {metric.split('_')[1]}: "
        
        if len(service) == 0:
            service = ['batch-service', 'auth-service', 'awsapi-service', 'front-service', 'main-service', 'prvt-service']
        
        for svc in service:
            response = cloudwatch.get_metric_statistics(
                    Namespace='ContainerInsights',
                    MetricName=metric,
                    Dimensions=[
                            {
                                'Name':'ClusterName',
                                'Value':f'tah-{stage}-eks-cluster'
                            },
                            {
                                'Name':'Namespace',
                                'Value':'default'
                            },
                            {
                                'Name':'Service',
                                'Value':svc
                            },
                        ],
                    StartTime=datetime.fromisoformat(time)-timedelta(hours=24),
                    EndTime=datetime.fromisoformat(time)-timedelta(hours=15),
                    Period=60,
                    Statistics=['Maximum']
                )
            point_list = [point['Maximum'] for point in response["Datapoints"] if point['Maximum']]
            maximum = max(point_list) if len(point_list) else 0
            text += f"{svc.split('-')[0]}({round(maximum,2)}%) "
        
        print(text)
    
def get_cluster_metrics(time):
    text = f"cluster: "
    
    for metric in cluster_metrics:
        response = cloudwatch.get_metric_statistics(
                Namespace='ContainerInsights',
                MetricName=metric,
                Dimensions=[
                        {
                            'Name':'ClusterName',
                            'Value':f'tah-{stage}-eks-cluster'
                        }
                    ],
                    StartTime=datetime.fromisoformat(time)-timedelta(hours=24),
                    EndTime=datetime.fromisoformat(time)-timedelta(hours=15),
                Period=60,
                Statistics=['Maximum']
            )
        
        maximum = max([point['Maximum'] for point in response["Datapoints"]])
        text += f"{metric.split('_')[1]}({round(maximum,2)}%) " if metric.split('_')[0] != 'cluster' else f"{metric.split('_')[1]}({math.trunc(maximum)}대) "
    
    print(text)    

def lambda_handler(event, context):
    time = event['time'].replace('Z', '')
    
    try:
        print("########## Writing system monitroing ##########")
        print({
            "StartTime": datetime.fromisoformat(time)-timedelta(hours=24),
            "EndTime": datetime.fromisoformat(time)-timedelta(hours=15)
        })
        get_cluster_metrics(time)
        get_service_metrics(time)
    finally:
        print("########## End Lambda Function ##########")