import os
import boto3

s3_client=boto3.client('s3', region_name=os.environ.get('AWS_DEFAULT_REGION'))
bucket_name=os.environ.get('BUCKET_NAME')

print("Creating the s3 bucket")
s3_client.create_bucket(
  Bucket=bucket_name,
  CreateBucketConfiguration={
    'LocationConstraint': region
  }
)

print("Removing public access")
s3_client.put_public_access_block(
  Bucket=bucket_name,
  PublicAccessBlockConfiguration={
    'BlockPublicAcls': True,
    'IgnorePublicAcls': True,
    'BlockPublicPolicy': True,
    'RestrictPublicBuckets': True
  }
)