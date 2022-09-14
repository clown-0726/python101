import json
import os
from settings import REQUEST_HOST, JWT_TOKEN
import requests

headers = {
    "authorization": JWT_TOKEN
}

"""测试 Commodity 新增"""
if False:
    res = requests.post(url=os.path.join(REQUEST_HOST, 'cmd/commodity_list'), data={
        'name': 'C20',
        'desc': 'C20',
    }, headers=headers)
    print(json.loads(res.content))

"""测试 Commodity 修改"""
if False:
    res = requests.put(url=os.path.join(REQUEST_HOST, 'cmd/commodity/e685533c694c4251a5755563d4cf1774/'), data={
        'name': 'C5',
        'desc': 'C5',
    }, headers=headers)
    print(json.loads(res.content))

"""测试得到一个 Commodity"""
if False:
    res = requests.get(url=os.path.join(REQUEST_HOST, 'cmd/commodity/e685533c694c4251a5755563d4cf1774/'), headers=headers)
    print(json.loads(res.content))

"""测试得到所有 Commodity"""
if False:
    res = requests.get(url=os.path.join(REQUEST_HOST, 'cmd/commodity_list'), headers=headers)
    print(json.loads(res.content))

if __name__ == '__main__':
    pass
