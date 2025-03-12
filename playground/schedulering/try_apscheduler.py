from apscheduler.schedulers.background import BackgroundScheduler
import time


# 定义一个任务函数
def my_job():
    print("任务正在运行...", time.strftime("%Y-%m-%d %H:%M:%S"))


# 创建调度器
scheduler = BackgroundScheduler()

# 添加任务：每隔 5 秒执行一次
scheduler.add_job(my_job, 'interval', seconds=5)

# 启动调度器
scheduler.start()

try:
    # 模拟主程序运行
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    # 停止调度器
    scheduler.shutdown()
    print("调度器已关闭")
