import boto3

client = boto3.client('ec2')
print("Stopping Instances.......")
response = client.stop_instances(
    InstanceIds=[
        'i-0b70e13d9b7ef2ff5',
    ],
)
print(response)