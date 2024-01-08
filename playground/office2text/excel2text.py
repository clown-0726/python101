import pandas as pd

'''
pip install openpyxl
pip install xlrd
pip install pandas

参考连接：https://www.ttt5.cn/72742.html
'''

data = pd.read_excel('./asset/a01b7fc1.xlsx')
data.to_csv('./123.txt', sep=';', header=True, encoding='utf_8_sig', index=False)

if __name__ == '__main__':
    pass
