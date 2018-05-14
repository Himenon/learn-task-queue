import multiprocessing as mp
from time import sleep

def washer(dishes, output):
    for dish in dishes:
        print("Washing", dish, "dish")
        output.put(dish)


def dryer(input):
    while True:
        sleep(5)
        dish = input.get()
        print("Drying", dish, "dish")
        input.task_done()


my_queue = mp.JoinableQueue()
proc = mp.Process(target=dryer, args=(my_queue,))
proc.daemon = True
proc.start()

dishes = ["salad", "bread", "entree", "dessert"]

washer(dishes, dish_queue)
dish_queue.join() # Queueの中身を取り出すまでブロック中
