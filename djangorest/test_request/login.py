import json
import os
from settings import REQUEST_HOST
import requests

"""获取 JWT 的 token"""
res = requests.post(url=os.path.join(REQUEST_HOST, 'login/'), json={
    "username": "admin",
    "password": "admin"
})

print(json.loads(res.content))

if __name__ == '__main__':
    pass
