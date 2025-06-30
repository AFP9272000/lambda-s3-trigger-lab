import boto3
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    
    # Download the uploaded file
    download_path = f'/tmp/{file_key}'
    s3.download_file(source_bucket, file_key, download_path)
    
    # Read file contents
    with open(download_path, 'r') as f:
        contents = f.read().strip()
    
    # Check for deploy=true
    if 'deploy=true' in contents:
        print("✅ Deployment started")

        # Create deployment.txt
        new_file_path = '/tmp/deployment.txt'
        with open(new_file_path, 'w') as f:
            f.write("🚀 Deployment succeeded!")
        
        # Upload to target bucket
        target_bucket = 'addison-bucket-deployment-12345'  # Change this!
        s3.upload_file(new_file_path, target_bucket, 'deploymenttrigger.txt')
        
    else:
        print("❌ No deployment triggered")
