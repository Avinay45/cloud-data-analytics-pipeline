import os
import boto3

from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv(
        "AWS_SECRET_ACCESS_KEY"
    ),
    region_name=os.getenv("AWS_REGION")
)

bucket_name = os.getenv(
    "S3_BUCKET_NAME"
)

files = [
    "customers.csv",
    "products.csv",
    "orders.csv"
]

for file_name in files:

    local_path = f"data/raw/{file_name}"

    s3.upload_file(
        local_path,
        bucket_name,
        f"raw/{file_name}"
    )

    print(f"Uploaded {file_name}")

print("All Files Uploaded")