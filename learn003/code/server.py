from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from os import environ
import redis
import json
import uuid

app = Flask(__name__)
api = Api(app)

CONN = redis.Redis(
    host=environ.get('REDIS_HOST'),
    port=environ.get('REDIS_PORT'),
    db=environ.get('REDIS_DB'))


class LongTaskResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('number', type=int, help='number type is ianteger.')
    TASK_PREFIX = 'long-task-'

    def post(self):
        args = self.parser.parse_args()
        number = args.get('number')
        queue_id = '{}{}'.format(self.TASK_PREFIX, str(uuid.uuid4()))
        msg = {'number': number, 'uuid': queue_id}

        CONN.lpush('my-queue', json.dumps(msg))

        response = jsonify(result_id=queue_id)
        response.status_code = 200
        return response


class TaskResultResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('result_id', type=str, help='result_id is str')

    def get(self):
        args = self.parser.parse_args()
        result_id = args.get('result_id')
        value = CONN.hget('result', result_id)
        if value:
            data = json.loads(value.decode('utf-8'))
            response = jsonify({'task_status': 'finish', 'data': data})
        else:
            response = jsonify({'task_status': 'wait'})
        response.cache_control.max_age = 60
        return response


api.add_resource(LongTaskResource, '/task')
api.add_resource(TaskResultResource, '/result')

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
