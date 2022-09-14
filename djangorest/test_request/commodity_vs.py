import json
import os
from settings import REQUEST_HOST, JWT_TOKEN
import requests

headers = {
    "authorization": JWT_TOKEN
}

# vs -------------------------------------------
"""测试得到所有 Commodity"""
if True:
    res = requests.get(url=os.path.join(REQUEST_HOST, 'cmd/commodity_list_vs?search=C2'), headers=headers)
    print(json.loads(res.content))

if __name__ == '__main__':
    pass
