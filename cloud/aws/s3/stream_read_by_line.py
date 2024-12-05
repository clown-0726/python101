import boto3
import tracemalloc

s3 = boto3.client('s3')

tracemalloc.start()

bucket_name = 'filing-reports'
file_key = 'txt-vector/reports-data/stock_gr/2022/09/30/4d6f9c5e-83ec-3ba6-aae1-e59c755d41a7.pdf/blocks.txt'

response = s3.get_object(Bucket=bucket_name, Key=file_key)
streaming_body = response['Body']

# 建立一个基于流读取的迭代器
for line in streaming_body.iter_lines():
    if line:
        # 处理每一行数据
        print(line.decode('utf-8'))

        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage is {current / 10 ** 6}MB, Peak was {peak / 10 ** 6}MB.")

tracemalloc.stop()
