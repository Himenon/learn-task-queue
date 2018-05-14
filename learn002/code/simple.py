from multiprocessing import Pool
from time import sleep
def f(x):
  sleep(5)
  return x*x

# https://docs.python.jp/3/library/multiprocessing.html
if __name__ == '__main__':
  with Pool(5) as p:
    print(p.map(f, [1, 2, 3]))
