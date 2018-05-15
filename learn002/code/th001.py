import threading
from time import sleep
import os

def info(title):
    template = """
    | {title}
    | --------------------------
    | module name : {name}
    | parent  pid : {ppid}
    | current pid : {pid}
    """
    print(template.format(title=title, name=__name__, 
        ppid=os.getppid(), pid=os.getpid()
    ))

def myfunc(name):
    info('Sub')
    print('Hello', name)
    while True:
      sleep(1)

if __name__ == '__main__':
    info('Main')
    for i in range(5):
        t = threading.Thread(target=myfunc, args=('おはよー！',))
        t.start()
