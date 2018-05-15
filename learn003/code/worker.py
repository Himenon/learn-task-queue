from os import environ
from time import sleep
import redis

r = redis.Redis(host=environ.get('REDIS_HOST'), port=environ.get('REDIS_PORT'))


def work(payload):
    if payload:
        print(payload)


if __name__ == '__main__':
    while True:
        work(r.lpop('my-queue'))
        sleep(0.02)
