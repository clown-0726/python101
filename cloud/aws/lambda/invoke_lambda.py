import base64
import boto3
import json

"""
InvocationType
    RequestResponse 同步调用
    Event 异步调用
ClientContext
    传递上下文信息
LogType='Tail'
    当你设置 LogType='Tail' 时，Lambda 会在响应中返回函数执行的最后 4 KB 的日志数据（Base64 编码）。
"""


def invoke_async():
    lambda_client = boto3.client('lambda')

    lambda_client.invoke(
        FunctionName='example',
        InvocationType='Event',
        Payload=json.dumps({"abc": "xyz"}, ensure_ascii=False),
    )


def invoke_sync():
    lambda_client = boto3.client('lambda')

    response = lambda_client.invoke(
        FunctionName='example',
        InvocationType='RequestResponse',
        Payload=json.dumps({"abc": "xyz"}, ensure_ascii=False),
    )
    response_payload = json.loads(response['Payload'].read().decode('utf-8'))
    print(response_payload)


def invoke_sync_with_context():
    lambda_client = boto3.client('lambda')
    client_context_json = json.dumps({
        'custom': {
            'timeout': 60 * 2
        }
    })
    client_context_encoded = base64.b64encode(client_context_json.encode('utf-8')).decode('utf-8')

    response = lambda_client.invoke(
        FunctionName='example',
        InvocationType='RequestResponse',
        Payload=json.dumps({"abc": "xyz"}, ensure_ascii=False),
        ClientContext=client_context_encoded,
    )
    response_payload = json.loads(response['Payload'].read().decode('utf-8'))
    print(response_payload)


if __name__ == "__main__":
    # invoke_async()
    # invoke_sync()
    invoke_sync_with_context()
