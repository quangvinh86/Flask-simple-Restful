import json
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)

PARSER = reqparse.RequestParser()
PARSER.add_argument('data')


TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': 'flask - rest-api'},
    'todo3': {'task': 'flask - restful-'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))




class Todo(Resource):
    """
    Shows a single todo item and lets you delete a todo item
    """
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        args = PARSER.parse_args()
        data = args['data']
        dict_data = json.loads(data)
        TODOS[todo_id] = dict_data
        return jsonify(todo_id=todo_id, data=dict_data)


class TodoList(Resource):
    """
    hows a list of all todos, and lets you POST to add new tasks
    """
    def get(self):
        return TODOS, 200

    def post(self):
        args = PARSER.parse_args()
        data = args['data']
        dict_data = json.loads(data)
        todo_id = 'todo{}'.format(int(max(TODOS.keys()).lstrip('todo')) + 1)
        TODOS[todo_id] = dict_data
        return jsonify(todo_id=todo_id, data=dict_data)

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
