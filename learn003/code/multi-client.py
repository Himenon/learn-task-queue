import threading
import requests
from retrying import retry
from datetime import datetime as dt
from logging import getLogger, INFO, basicConfig

logger = getLogger(__name__)
basicConfig(level=INFO)


def register_task(number):
    params = {'number': number}
    response = requests.post('http://localhost:5000/task', params=params)
    result_id = response.json().get('result_id')
    return result_id


@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000)
def get_task_result(result_id):
    params = {'result_id': result_id}
    response = requests.get('http://localhost:5000/result', params=params)
    data = response.json()
    if data.get('task_status') != 'finish':
        logger.info("[{}] Retryします".format(dt.now()))
        raise response.raise_for_status()
    return data


def my_request(number):
    result_id = register_task(number)
    data = get_task_result(result_id)
    print(data)


if __name__ == '__main__':
    for i in range(50):
        t = threading.Thread(target=my_request, args=(i, ))
        t.start()
