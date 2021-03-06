from multiprocessing import Process
import os
from time import sleep


def info(title):
    template = """
    | {title}
    | --------------------------
    | module name : {name}
    | parent  pid : {ppid}
    | current pid : {pid}
    """
    print(
        template.format(
            title=title, name=__name__, ppid=os.getppid(), pid=os.getpid()))


def myfunc(name):
    info('Sub')
    print('Hello', name)


if __name__ == '__main__':
    info('Main')
    p = Process(target=myfunc, args=('おけまる', ))
    while True:
        sleep(1)
    p.start()
    p.join()
