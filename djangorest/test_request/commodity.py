import json
import os
from settings import REQUEST_HOST
import requests

headers = {
    "authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNjYyOTQ0Nzc5LCJleHAiOjE2NjMwMzExNzksImp0aSI6ImZiNDI5OWFhLTFlMjUtNDc2Ny05ZGVlLWQ4ZGFhZGMyNmIwYSIsInVzZXJfaWQiOjEsIm9yaWdfaWF0IjoxNjYyOTQ0Nzc5fQ.4DfS04iz2xquRXByLBjJ3tMZwL3RBHu3rBT7CR4J5m0"
}

"""测试 LoginRequiredMixin"""
if False:
    res = requests.post(url=os.path.join(REQUEST_HOST, 'commodity/auth_test'), headers=headers)
    print(json.loads(res.content))

"""测试 Commodity 新增"""
if False:
    res = requests.post(url=os.path.join(REQUEST_HOST, 'commodity/commodity_edit'), data={
        'name': 'C3',
        'desc': 'C3',
    }, headers=headers)
    print(json.loads(res.content))

"""测试 Commodity 修改"""
if True:
    res = requests.put(url=os.path.join(REQUEST_HOST, 'commodity/commodity/18e5b6b6c3b644a48f49708a88b3a5fb/'), data={
        'name': 'C5',
        'desc': 'C5',
    }, headers=headers)
    print(json.loads(res.content))

"""测试得到一个 Commodity"""
if False:
    res = requests.get(url=os.path.join(REQUEST_HOST, 'commodity/commodity/18e5b6b6c3b644a48f49708a88b3a5fb/'), headers=headers)
    print(json.loads(res.content))

"""测试得到所有 Commodity"""
if False:
    res = requests.get(url=os.path.join(REQUEST_HOST, 'commodity/commodity_list'), headers=headers)
    print(json.loads(res.content))

if __name__ == '__main__':
    pass
