import boto3
import json

access_key = raw_input("Access Key: ")
secret_key = raw_input("Secret Key: ")

ec2 = boto3.client(
    'ec2',
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='us-west-2')

response = ec2.describe_instances()
del response["ResponseMetadata"]
with open('describe-instances.json', 'w') as fp:
    fp.write(json.dumps(response, indent=4, default=str))



