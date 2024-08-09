import time
from threading import Thread


def schedule_task(task, interval):
    def task_wrapper():
        while True:
            task()
            time.sleep(interval)

    thread = Thread(target=task_wrapper)
    thread.start()
