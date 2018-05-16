import multiprocessing as mp
from time import sleep
import os


def info(title):
    template = """
    {title}
    | module name: {name}
    | parent process: {ppid}
    | process id: {pid}
    """
    print(
        template.format(
            title=title, name=__name__, ppid=os.getppid(), pid=os.getpid()))


def washer(dishes, output):
    for dish in dishes:
        pid = os.getpid()
        print("[{}] Washing {} dish".format(pid, dish))
        output.put(dish)


def dryer(_input):
    info("dryer")
    while True:
        sleep(5)
        dish = _input.get()
        pid = os.getpid()
        print("[{}] Drying {} dish".format(pid, dish))
        _input.task_done()


my_queue = mp.JoinableQueue()
proc = mp.Process(target=dryer, args=(my_queue, ))
proc.daemon = True
proc.start()

dishes = ["salad", "bread", "entree", "dessert"]

washer(dishes, my_queue)
my_queue.join()  # Queueの中身を取り出すまでブロック中
