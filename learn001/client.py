import redis
from os import environ
from time import sleep

r = redis.Redis(host=environ.get('REDIS_HOST'), port=environ.get('REDIS_PORT'))

if __name__ == '__main__':
  r.lpush('my-queue', 'hello')
 