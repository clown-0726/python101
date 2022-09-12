import pandas as pd

df = pd.read_csv('./HR.csv')

# pandas.core.series.Series 是组成 pandas.core.frame.DataFrame 的列数据
# 一般来说，这两种数据结构的操作都是公用的
print(type(df))
print(type(df['satisfaction_level']))

# 均值
print(df.mean())
print(df['satisfaction_level'].mean())

# 中位数
print(df.median())
print(df['satisfaction_level'].median())

# 四分位数
print(df.quantile(q=0.25))
print(df['satisfaction_level'].quantile(q=0.25))

# 众数
print(df.mode())
print(df['satisfaction_level'].mode())

# 标准差
print(df.std())
print(df['satisfaction_level'].std())

# 方差
print(df.var())
print(df['satisfaction_level'].var())

# 求和
print(df.sum())
print(df['satisfaction_level'].sum())

# 偏态系数
print(df.skew())
print(df['satisfaction_level'].skew())

# 峰态系数（以正态分布为基础）
print(df.kurt())
print(df['satisfaction_level'].kurt())

import scipy.stats as ss

# 正态分布
# m 均值
# v 方差
# 偏态系数
# 峰态系数
ss.norm.stats(moments='mvsk')

# 得到分布函数在坐标上的值
ss.norm.pdf(0.0)

# 得到分布函数在坐标上的累积值（必须是 0 到 1 之间）
ss.norm.pdf(0.9)

# 从负无穷累积到 2 的概率是多少
ss.norm.cdf(2)

# 其他三大分布函数
# T 分布
ss.t
# F 分布
ss.f
# 卡方分布
ss.chi2

# 抽样
print(df.sample(10))
print(df['satisfaction_level'].sample(10))

if __name__ == '__main__':
    pass
