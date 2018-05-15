import requests


def register_task(task_id):
    params = {'task_id': task_id}
    requests.get('http://localhost:5000/task', params=params)


def get_task_result(task_id):
    params = {'task_id': task_id}
    res = requests.get('http://localhost:5000/result', params=params)
    return res.json()


if __name__ == '__main__':
    register_task(1)
