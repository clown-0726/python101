import json

import requests

# API URL
url = "https://api.gleif.org/api/v1/lei-records/21380026UDE3LKFSDP68"

# 请求头
headers = {
    "Accept": "application/vnd.api+json"
}

# 发送 GET 请求
response = requests.get(url, headers=headers)

# 检查响应状态码
if response.status_code == 200:
    # 解析 JSON 响应
    data = response.json()
    print(json.dumps(data, ensure_ascii=False, indent=4))  # 打印完整的 JSON 数据
else:
    print(f"请求失败，状态码: {response.status_code}")
    print(response.text)  # 打印错误信息
