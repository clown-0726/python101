import json
import os
from settings import REQUEST_HOST, JWT_TOKEN
import requests

headers = {
    "authorization": JWT_TOKEN
}

"""测试得到所有 Commodity"""
if False:
    res = requests.get(url=os.path.join(REQUEST_HOST, 'cmd/commodity_list_ga'), headers=headers)
    print(json.loads(res.content))

if __name__ == '__main__':
    pass
