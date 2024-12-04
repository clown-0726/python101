import boto3


def loop_objects():
    s3_client = boto3.client('s3')
    bucket = "ot-cdn"
    prefix = "crunchbase/data-html/"

    count = 1
    continuation_token = None
    while True:
        if continuation_token:
            response = s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix, ContinuationToken=continuation_token)
        else:
            response = s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)
        # 得到内容
        if 'Contents' in response:
            for item in response['Contents']:
                count += 1
                print(count, item["Key"])

        # 检查是否还有更多对象
        if response.get('IsTruncated'):  # 如果返回结果被截断
            continuation_token = response.get('NextContinuationToken')
        else:
            break


if __name__ == "__main__":
    loop_objects()
