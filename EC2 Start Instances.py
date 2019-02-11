import boto3

client = boto3.client('ec2')

print("Starting Instances.......")
response = client.start_instances(
    InstanceIds=[
        'i-0b70e13d9b7ef2ff5',
    ],
)
print(response)