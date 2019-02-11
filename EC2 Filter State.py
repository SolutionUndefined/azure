import boto3

ec2 = boto3.resource('ec2')

ec2.filter = [{'Name': 'instance-state-name', 'Values': ['running']}]
# for instance in ec2.filter:
#    print(instance.id, instance.instance_type)

print("Stopping running instances......")
ec2.instances.filter(Filters=ec2.filter).stop()
