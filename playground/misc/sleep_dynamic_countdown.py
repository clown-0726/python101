import random
import time

if __name__ == '__main__':
    # 随机睡觉几秒
    remaining_time = int(random.uniform(5, 10))
    while remaining_time > 0:
        print(f"\r倒计时: {remaining_time} 秒", end="", flush=True)
        time.sleep(1)
        remaining_time -= 1
    print()  # 换行
