import boto3

default_region = 'us-east-1'
region_two = 'ap-south-1'
s3_client = boto3.client('s3',default_region)

def delete_bucket(bucket_name) :
    response= s3_client.delete_bucket(Bucket=bucket_name)
    print(response)
    print(type(response))

def create_bucket(bucekt_name):
    response =s3_client.create_bucket(ACL='private',Bucket=bucekt_name,CreateBucketConfiguration={'LocationConstraint':default_region})
    print(response)


if __name__ == '__main__':
    response = s3_client.list_buckets()
    for bucket_name_dict in response['Buckets']:
        bucket_name=bucket_name_dict['Name']
        print(bucket_name)

