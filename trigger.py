# uploads files to s3

import boto3

s3 = boto3.client('s3', region_name='us-east-2')

bucket_name = 'addison-bucket-deployment-12345'  # must be globally unique


# Upload file
s3.upload_file('deploymenttrigger.txt', bucket_name, 'deploymenttrigger.txt')


print(f"✅ Uploaded 'deploymenttrigger.txt' to {bucket_name}")
