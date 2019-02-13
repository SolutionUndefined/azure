import boto3
import time
import re

ec2 = boto3.resource('ec2')
ids = []
instances = ec2.instances.filter(
    Filters=[{'Name': 'tag:team', 'Values': ['completelystrange']}])


for instance in instances:
	print("Working on " + instance.instance_id)
	response = instance.delete_tags(DryRun=False, Tags=[{'Key': 'team', 'Value': 'completelystrange'}])
	tag = instance.create_tags(DryRun=False, Tags=[{'Key': 'team', 'Value': 'x'}])
	print("Tags associated are now :")
	newTaglist = instance.tags	
	for z in list(newTaglist):
		print(z)
