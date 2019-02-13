import boto3
import time

ec2 = boto3.resource('ec2')

instances = ec2.instances.filter(
    Filters=[{'Name': 'tag:team', 'Values': ['completelystrange']}])

for instance in instances:
    print("Found instances tag with team completelystrange...")
    print(instance.id, instance.instance_type)
    time.sleep(5)

ec2_filter = [{'Name': 'tag:team', 'Values': ['completelystrange']}]
print("Stopping instances...")
ec2.instances.filter(Filters=ec2_filter).stop()
time.sleep(10)
