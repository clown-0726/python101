from contextlib import suppress

for attempt in range(3):
    try:
        print("打开一个资源，比如一个连接")
        # raise Exception("Err occur...")
        break
    except Exception as e:
        print(f"第 {attempt + 1} 次尝试失败，错误信息: {e}")
    finally:
        print("不管是正常执行（正常执行中有 break 关键词），还是出现异常，都会执行这里的代码！")
        with suppress(Exception):
            print("关闭打开的资源，比如一个连接")
else:
    print("尝试了 3 次，但仍然失败")
