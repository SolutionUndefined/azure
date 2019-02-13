import boto3
import time

ec2 = boto3.resource('ec2')
ids = []
instances = ec2.instances.filter(
    Filters=[{'Name': 'tag:team', 'Values': ['completelystrange']}])

for instance in instances:
	response = instance.delete_tags(
		Tags=[
			{
				'Key': 'team',
				'Value': 'completelystrange'
			},
		]
	)
	tag = instance.create_tags(
		Tags=[
			{
				'Key': 'team',
				'Value': 'completelyweird'
			},
			{
				'Key': 'Platform',
				'Value': 'Linux',
			},
		]
	)