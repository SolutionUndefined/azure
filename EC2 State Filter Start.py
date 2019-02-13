import boto3
import time

ec2 = boto3.resource('ec2')

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])

for instance in instances:
    print("Found running instances")
    print(instance.id, instance.instance_type)
    time.sleep(5)

ec2.filter = [{'Name': 'instance-state-name', 'Values': ['stopped']}]
print("Starting instances...")
ec2.instances.filter(Filters=ec2.filter).start()
time.sleep(10)
print("Initializing instances...")
