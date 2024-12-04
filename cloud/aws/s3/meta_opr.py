import boto3

'''
meta 信息分为两种，一种是系统的，一种是用户自定义的
System defined	Content-Type	    text/html;charset=utf-8
User defined    x-amz-meta-idxxx    value
'''


def put_object():
    s3_resource = boto3.resource('s3')

    bucket_name = "orbit-common-resources"
    object_name = "test/xxx.txt"

    # 创建的时候增加 Metadata
    object_put = s3_resource.Object(bucket_name, object_name)
    object_put.put(Body="xxxxx".encode('utf-8'), Metadata={'id-xxx': 'value123'}, ContentType='text/html;charset=utf-8')


def get_object_meta():
    s3_client = boto3.client('s3')

    bucket_name = "orbit-common-resources"
    object_name = "test/xxx.txt"

    # 获取数据的 Metadata
    response = s3_client.head_object(Bucket=bucket_name, Key=object_name)
    print(response['Metadata'])


def modify_object_meta():
    s3_resource = boto3.resource('s3')

    bucket_name = "orbit-common-resources"
    object_name = "test/xxx.txt"

    # 修改数据的 Metadata
    s3_object = s3_resource.Object(bucket_name, object_name)
    # 增加一个 id-yyy
    s3_object.metadata.update({
        'id-yyy': 'value123'
    })
    s3_object.copy_from(CopySource={'Bucket': bucket_name, 'Key': object_name},
                        Metadata=s3_object.metadata,
                        MetadataDirective='REPLACE')


if __name__ == "__main__":
    # put_object()
    # get_object_meta()
    modify_object_meta()
