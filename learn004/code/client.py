import redis
from datetime import datetime as dt
from logging import getLogger, INFO, basicConfig
from os import environ

logger = getLogger(__name__)
basicConfig(level=INFO)

CONN = redis.StrictRedis(
    host=environ.get('REDIS_HOST'),
    port=environ.get('REDIS_PORT'),
    db=environ.get('REDIS_DB'))

if __name__ == '__main__':
    p = CONN.pubsub()
    channel = environ.get('REDIS_SUBSCRIBE_CHANNEL')
    my_message = {'hello': 'world'}
    res = CONN.publish(channel, my_message)
    logger.info(res)
