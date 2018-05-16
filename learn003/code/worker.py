import redis
import json
from os import environ
from time import sleep
from datetime import datetime as dt
from logging import getLogger, INFO, basicConfig

logger = getLogger(__name__)
basicConfig(level=INFO)

CONN = redis.Redis(
    host=environ.get('REDIS_HOST'),
    port=environ.get('REDIS_PORT'),
    db=environ.get('REDIS_DB'))


def work():
    value = CONN.lpop('my-queue')
    if not value:
        return
    data = json.loads(value.decode('utf-8'))
    number = data.get('number')
    uuid = data.get('uuid')
    logger.info("[{}] Start Task : {}".format(dt.now(), uuid))
    sleep(5)
    logger.info("[{}] Finish Task: {}".format(dt.now(), uuid))
    CONN.hset('result', uuid, number * number)


if __name__ == '__main__':
    while True:
        work()
        sleep(0.02)
