import boto3
import time
import os
import re
from botocore.exceptions import ClientError

LOG_GROUP_NAME = 'log-test'


def put_log_events(log_path):
    client = boto3.client('logs')

    # Create log stream
    log_stream_name = os.path.basename(log_path)
    log_stream_name = re.findall(r'(.*?T\d{2}).', log_stream_name)[0]
    # log_date = log_stream_name[-13:-3]
    try:
        client.create_log_stream(
            logGroupName=LOG_GROUP_NAME,
            logStreamName=log_stream_name
        )
        print(f'Create log stream <{log_stream_name}> success.')
    except ClientError:
        print(f'Log stream <{log_stream_name}> already exist.')

    with open(log_path, 'rb') as f:
        lines = f.readlines()

    log_events_list = []
    for line in lines:
        log_events_list.append({
            'timestamp': int(time.time() * 1000),
            'message': line.decode('utf-8'),
        })

    # The maximum number of log events in a batch is 10,000. But it's best to only send 1000 at a time.
    for i in range(0, len(log_events_list), 1000):
        client.put_log_events(
            logGroupName=LOG_GROUP_NAME,
            logStreamName=log_stream_name,
            logEvents=log_events_list[i:i + 1000]
        )

    # os.remove(log_path)


if __name__ == '__main__':
    log_dir = 'spider_run_logs'

    # client = boto3.client('logs')

    # # Delete log group
    # client.delete_log_group(logGroupName=LOG_GROUP_NAME)

    # # Create log group
    # client.create_log_group(
    #     logGroupName=LOG_GROUP_NAME
    # )

    for log_file in os.listdir(log_dir):
        log_file_path = os.path.join(log_dir, log_file)
        put_log_events(log_file_path)
