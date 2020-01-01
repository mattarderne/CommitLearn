import boto3

s3_resource = boto3.resource('s3')
session = boto3.session.Session(profile_name='default')

import uuid
def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])


def create_bucket(bucket_prefix, s3_connection):
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
        'LocationConstraint': current_region})
    print(bucket_name, current_region)
    return bucket_name, bucket_response

# second_bucket_name, second_response = create_bucket(bucket_prefix='secondpythonbucket', s3_connection=s3_resource)
# print(second_bucket_name)

def list_buckets():
    for bucket in s3_resource.buckets.all():
        print(bucket.name)

def list_objects(bucketname):
    my_bucket = s3_resource.Bucket(bucketname)
    for file in my_bucket.objects.all():
        print(file.key)


def delete_s3(bucketname):
    '''
    Delete S3 bucket
    '''
    s3 = boto3.client('s3')
    response = s3.delete_bucket(Bucket=bucketname)
    return bucketname,response;

def write_json_s3(bucketname,objectname,data):
    '''
    Write JSON data to specified S3 object in a bucket, create bucket if not exist
    '''
    create_bucket(bucketname)
    
    s3 = boto3.resource('s3')
    obj = s3.Object(bucketname,f'{objectname}.json')
    response = obj.put(Body=json.dumps(data))
    
    return obj,response;

def upload_file(bucketname, filename):
    '''
    Load a file to a bucket
    '''
    response = s3_resource.meta.client.upload_file(filename, bucketname, filename)
    s3_resource.ObjectAcl(bucketname,filename).put(ACL='public-read')
    return response;