import requests

def register_task(task_id):
    params = {
      'task_id': task_id
    }
    res = requests.get('http://localhost:5000/task', params=params)
    print(res.json())

def get_result(task_id):
    params = {
      'task_id': task_id
    }
    res = requests.get('http://localhost:5000/result', params=params)
    if res.status_code == 200:
        return res.json()
    print(res.text)

if __name__ == '__main__':
    register_task(1)
