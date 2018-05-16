import redis
import json
from os import environ
from time import sleep
from datetime import datetime as dt
from logging import getLogger, INFO, basicConfig

logger = getLogger(__name__)
basicConfig(level=INFO)

CONN = redis.StrictRedis(
    host=environ.get('REDIS_HOST'),
    port=environ.get('REDIS_PORT'),
    db=environ.get('REDIS_DB'))


def work(message):
    logger.info(message)


if __name__ == '__main__':
    p = CONN.pubsub()
    channel = environ.get('REDIS_SUBSCRIBE_CHANNEL')
    p.subscribe(channel)
    while True:
        message = p.get_message()
        if message:
            work(message)
        sleep(0.001)
