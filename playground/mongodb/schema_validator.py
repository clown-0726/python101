from pymongo import MongoClient, ReadPreference

# 连接 MongoDB
client = MongoClient("YOUR CONNECTION HERE")

# 选择数据库和集合
db = client['filing_reports']
collection = db.get_collection('filing_data', read_preference=ReadPreference.SECONDARY)

# 获取集合的 schema（验证器）
coll_info = db.command("listCollections", filter={"name": "filing_data"})
validator = coll_info['cursor']['firstBatch'][0].get('options', {}).get('validator', {})

print(validator)

# 查询不符合 schema 的文档
# 注意：$nor 需要是一个条件数组，validator 本身可能需要转换为条件表达式
results = collection.find({"$nor": [validator]}).limit(10)

# 打印结果
for doc in results:
    print(doc)
