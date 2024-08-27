from ftplib import FTP, error_perm

"""
必须使用 python 3.8 以上
"""

ftp_server = ''
ftp_user = ''
ftp_password = ''
remote_file_path = '700/2024/8/25/慧选图表资讯0825.pdf'
local_file_path = 'file.pdf'

# 目标目录
target_directory = '/700/2024/8/25/'

# 创建 FTP 对象并连接到服务器
ftp = FTP(ftp_server, encoding='GB2312')
ftp.login(user=ftp_user, passwd=ftp_password)

# 打开本地文件以写入二进制数据
with open(local_file_path, 'wb') as local_file:
    # 使用 FTP 的 retrbinary 方法下载文件
    ftp.retrbinary(f'RETR {remote_file_path}', local_file.write)


def list_files(ftp):
    files = []
    ftp.retrlines('LIST', files.append)
    return files


# 切换到目标目录
try:
    ftp.cwd(target_directory)
    print(f"Changed to directory: {target_directory}")

    # 列出目标目录内容
    files = list_files(ftp)
    for file in files:
        print(file)
except error_perm as e:
    print(f"Failed to change to directory {target_directory}: {e}")

# 关闭FTP连接
ftp.quit()
