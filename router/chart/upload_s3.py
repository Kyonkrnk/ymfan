import boto3
import json

with open("config.json", encoding="utf-8") as f:
    config = json.load(f)

r2 = boto3.resource("s3",
  endpoint_url = config["endpoint_url"],
  aws_access_key_id = config["aws_access_key_id"],
  aws_secret_access_key = config["aws_secret_access_key"]
)
bucket = r2.Bucket(config["bucket_name"])

def upload_s3(content, path):
    bucket.put_object(Key=path, Body=content)