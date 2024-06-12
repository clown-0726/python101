import boto3

s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')

bucket_name = 'xiaoma-test'
object_name = 'filing_file/xxxxxxxx.txt'

# 创建的时候增加 Metadata
object_put = s3_resource.Object(bucket_name, object_name)
object_put.put(Body="xxxxx".encode('utf-8'), Metadata={'id-xxx': 'value123'}, ContentType='text/html;charset=utf-8')

# 获取数据的 Metadata
# response = s3_client.head_object(Bucket=bucket_name, Key=object_name)
# print(response['Metadata'])

# 修改数据的 Metadata
# s3_object = s3_resource.Object(bucket_name, object_name)
# s3_object.metadata.update({
#     'idzzz': 'value123'
# })
# s3_object.copy_from(CopySource={'Bucket': bucket_name, 'Key': object_name}, Metadata=s3_object.metadata, MetadataDirective='REPLACE')

'''
System defined	Content-Type	    text/html;charset=utf-8
User defined    x-amz-meta-idxxx    value
'''
