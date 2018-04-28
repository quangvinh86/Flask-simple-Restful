**Bước 1**: Tạo virtual environment, cài vào các thư viện sau:



```
pip install flask
pip install flask-sqlachemy
pip install flask_restful
pip install flask_cors
```


**Bước 2**: Tạo ứng dụng flask:

```Python
import json
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

```


**Bước 3**: Cài phần mềm Postman vào chorme:

kiểm tra: GET-http://127.0.0.1:5000/


**Bước 4**: Tạo cấu trúc dữ liệu TODOS và class TodoListAPI



```Python

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': 'flask - rest-api'},
    'todo3': {'task': 'flask - restful-api'},
}


class TodoList(Resource):
    """
    hows a list of all todos, and lets you POST to add new tasks
    """
    def get(self):
        return TODOS, 200


api.add_resource(TodoList, '/todos')


if __name__ == '__main__':
    app.run(debug=True, port=5000)

```


Dùng postman thử kết quả:
```
http://localhost:5000/todos/
```


**Bước 5**: Truy vấn dữ liệu 1 bản ghi:


Tạo class Todo xử lý các dữ liệu liên quan đến 1 bản ghi

```Python
class Todo(Resource):
    """
    Shows a single todo item and lets you delete a todo item
    """
    def get(self, todo_id):
        return TODOS[todo_id]

    def delete(self, todo_id):
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        pass

api.add_resource(Todo, '/todos/<todo_id>')
```

Dùng postman thực hiện test get/delete 1 bản ghi:

```
http://localhost:5000/todos/todo1

```

**Bước 6**: Xử lý trường hợp không có bản ghi:

Thêm function:

```Python


TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': 'flask - rest-api'},
    'todo3': {'task': 'flask - restful-'},
}



def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))
```

Thêm code:

```Python


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
        pass



```

Dùng postman post thử dữ liệu

**Bước 7**: Xử lý trường hợp add thêm bản ghi:

Thêm phần truy vấn args truyền vào:

```
app = Flask(__name__)
api = Api(app)

PARSER = reqparse.RequestParser()
PARSER.add_argument('data')
``


```Python
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
        return TODOS[todo_id], 201

```


Dùng postman, chọn body:
key: data
value: {'task': 'demo post'}


**Bước 8**: Put dữ liệu

Sửa lại hàm put

```Python
    def put(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        args = PARSER.parse_args()
        data = args['data']
        dict_data = json.loads(data)
        TODOS[todo_id] = dict_data
        return jsonify(todo_id=todo_id, data=dict_data)

```

Dùng postman put dữ liệu.

