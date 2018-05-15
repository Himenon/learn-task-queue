import threading
import queue
import time
import os


def washer(dishes_, dish_queue_):
    for dish in dishes_:
        pid = os.getpid()
        print("[{}] Washing {} dish".format(pid, dish))
        time.sleep(5)
        dish_queue_.put(dish)


def dryer(dish_queue_):
    while True:
        dish = dish_queue_.get()
        pid = os.getpid()
        print("[{}] Drying {} dish".format(pid, dish))
        time.sleep(10)
        dish_queue_.task_done()


dish_queue = queue.Queue()
for n in range(4):
    dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
    dryer_thread.start()
    print("スレッド増えたお")

dishes = ['1. salad', '2. bread', '3. entree', '4. desert']
washer(dishes, dish_queue)
dish_queue.join()
