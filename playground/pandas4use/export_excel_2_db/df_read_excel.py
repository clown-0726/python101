import pandas as pd
from sqlalchemy import create_engine

df = pd.read_excel("sample_company.xlsx", sheet_name="Sheet1")
df = df.rename(columns={
    'ID': 'dei_id',
    'Name': 'name',
    'Legal Entity Identifier': 'lei',
    'Ticker symbol': 'ticker',
    'Location Country': 'country',
    'Website': 'website',
})

# 对所有数据进行 strip 操作
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

print(df)

# 创建一个 PostgreSQL 连接引擎
engine = create_engine('postgresql://username:password@host:5432/db')

# 将 DataFrame 输出到 PostgreSQL
df.to_sql('sample_company', engine, if_exists='replace', index=False)
