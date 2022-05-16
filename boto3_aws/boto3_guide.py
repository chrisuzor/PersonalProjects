import uuid

import boto3


def create_bucket_name(bucket_prefix):
    return "".join([bucket_prefix, str(uuid.uuid4())])


def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    if current_region == "us-east-1":
        bucket_response = s3_connection.create_bucket(Bucket=bucket_name)
    else:
        bucket_response = s3_connection.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={"LocationConstraint": current_region},
        )
    print(bucket_name, current_region)
    return bucket_name, bucket_response


def create_temp_files(size, file_name, file_content):
    random_file_name = "".join([str(uuid.uuid4().hex[:6]), file_name])
    with open(random_file_name, "w") as f:
        f.write(str(file_content) * size)
    return random_file_name


def copy_to_bucket(s3_connection, from_bucket, to_bucket, file_name):
    copy_source = {"Bucket": from_bucket, "Key": file_name}

    s3_connection.Object(to_bucket, file_name).copy(copy_source)
