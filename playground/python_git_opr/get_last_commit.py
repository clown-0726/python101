import subprocess


def get_git_commit():
    try:
        # 运行git命令获取提交版本
        result = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True)

        if result.returncode == 0:
            # 提取提交版本
            commit_hash = result.stdout.strip()
            return commit_hash
        else:
            # Git命令执行失败
            print("Git命令执行失败:", result.stderr)
            return None
    except FileNotFoundError:
        # Git命令未找到
        print("Git命令未找到，请确保Git已正确安装并配置环境变量。")
        return None


# 获取当前提交版本
commit_version = get_git_commit()
if commit_version:
    print("当前提交版本:", commit_version)

# 0482ccb8cd21ded33cf1643d29500c9b90c56d04
