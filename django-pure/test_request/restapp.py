import json
import os
from settings import REQUEST_HOST
import requests

headers = {
    "authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNjYyOTI0Nzk3LCJleHAiOjE2NjMwMTExOTcsImp0aSI6ImM1NmVhZDUwLWY3MTEtNGViMS1iMWM4LTNmNTQ1MDIxYjEwZCIsInVzZXJfaWQiOjEsIm9yaWdfaWF0IjoxNjYyOTI0Nzk3fQ.gbHR5NNu8L9rdBXuLuZKSiIRB-dcnIvhZSjY0STyFEk"
}

"""测试 LoginRequiredMixin"""
if False:
    res = requests.post(url=os.path.join(REQUEST_HOST, 'restapp/auth_test'), headers=headers)
    print(json.loads(res.content))

"""测试 Commodity 新增"""
if True:
    res = requests.post(url=os.path.join(REQUEST_HOST, 'restapp/commodity_edit'), data={
        'name': 'C#',
        'desc': 'C#',
    }, headers=headers)
    print(json.loads(res.content))

"""测试得到一个 Commodity"""
if False:
    res = requests.get(url=os.path.join(REQUEST_HOST, 'restapp/commodity/7b8caa3fea284382b16fd1b7db3516c5'), headers=headers)
    print(json.loads(res.content))

"""测试得到所有 Commodity"""
if False:
    res = requests.get(url=os.path.join(REQUEST_HOST, 'restapp/commodity_list'), headers=headers)
    print(json.loads(res.content))

if __name__ == '__main__':
    pass
