from flask import Flask, abort, make_response, jsonify
from flask_restful import Api, Resource, reqparse
from os import environ
import redis
import json

app = Flask(__name__)
api = Api(app)

r = redis.Redis(host=environ.get('REDIS_HOST'), port=environ.get('REDIS_PORT'))

class LongTaskResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('task_id', type=int, help='task_id type is integer.')

    def get(self):
        args = self.parser.parse_args()
        task_id = args.get('task_id')
        msg = { 'task_id': task_id }
        redis_response = r.lpush('my-queue', json.dumps(msg))
        if redis_response:
            response = jsonify(
                message='Success register task {}'.format(task_id), 
                result_url='http://localhost:5000/result?task_id={}'.format(task_id)
            )
            response.status_code = 400
            return response
        else:
            response = jsonify(message='Failed Register Task {}'.format(task_id))
            response.status_code = 400
            return response

    def post(self):
        args = self.parser.parse_args()
        task_id = args.get('task_id')
        print(task_id)
        return make_response(msg)

class TaskResultResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('task_id', type=int, help='Task Id')
    def get(self):
        args = self.parser.parse_args()
        task_id = args.get('task_id')

api.add_resource(LongTaskResource, '/task')

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
