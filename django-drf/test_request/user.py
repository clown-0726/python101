import json
import os
from test_request.settings import REQUEST_HOST, JWT_TOKEN
import requests

headers = {
    "authorization": JWT_TOKEN
}

"""获取 JWT 的 token"""
if False:
    res = requests.post(url=os.path.join(REQUEST_HOST, 'login/'), json={
        "username": "admin",
        "password": "admin"
    })

    print(json.loads(res.content))

"""测试 LoginRequiredMixin"""
if False:
    res = requests.post(url=os.path.join(REQUEST_HOST, 'user/auth_test'), headers=headers)
    print(json.loads(res.content))

if __name__ == '__main__':
    pass
