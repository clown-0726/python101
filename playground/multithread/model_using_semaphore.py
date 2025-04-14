import time
from threading import Thread, Semaphore


class SemTaskProcessor(Thread):
    def __init__(self, sem_in: Semaphore, ind_in, task_in):
        self.sem_in = sem_in
        self.ind_in = ind_in
        self.task_in = task_in

        super(SemTaskProcessor, self).__init__(name=f"SemTaskProcessor-{str(self.ind_in)}")

    def run(self):
        print(f">>>>>> Start Processing {str(self.ind_in)} {self.task_in}\n")
        try:  # 一定要用 try 保证 Semaphore 能够被顺利释放
            time.sleep(1)
        except Exception as e:
            print(e)

        self.sem_in.release()  # 释放 sem


if __name__ == "__main__":
    max_thread_pool = 10
    sem = Semaphore(max_thread_pool)

    # 设置一批要处理的任务
    tasks_cache = []
    for _ in range(100):
        tasks_cache.append({"name": "name-1", "content": "fol"})

    threads = []  # 保存所有线程任务
    for ind, item_task in enumerate(tasks_cache, start=1):
        sem.acquire()
        html_thread = SemTaskProcessor(sem_in=sem, ind_in=ind, task_in=item_task)
        html_thread.start()
        threads.append(html_thread)

    # 等待所有线程完成
    for t in threads:
        t.join()
    print("所有任务处理完成。")
