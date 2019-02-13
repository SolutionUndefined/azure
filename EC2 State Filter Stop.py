import boto3
import time

ec2 = boto3.resource('ec2')

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

for instance in instances:
    print("Found running instances")
    print(instance.id, instance.instance_type)
    time.sleep(5)

ec2.filter = [{'Name': 'instance-state-name', 'Values': ['running']}]
print("Stopping instances...")
ec2.instances.filter(Filters=ec2.filter).stop()
time.sleep(10)
print("Instances has been stopped")



