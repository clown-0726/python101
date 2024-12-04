import boto3


def put_object():
    s3_resource = boto3.resource('s3')

    bucket_name = "orbit-common-resources"
    object_name = "test/xxx.txt"

    object_put = s3_resource.Object(bucket_name, object_name)
    object_put.put(Body="abc".encode('utf-8'))


if __name__ == "__main__":
    put_object()
