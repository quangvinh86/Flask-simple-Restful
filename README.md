# Flask-simple-Restful
Create a basic RestFul API with flask

http://flask-restful.readthedocs.io/en/latest/quickstart.html

## Phần 1: GET
1. Tạo một virtual enviromnent với tên: Flask-simple-Restful
Thực hiện install các gói trong requirements.txt vào VE
2. Download và copy database demo của SQLite3: chinook.db

http://www.sqlitetutorial.net/sqlite-sample-database/

3. Tạo một project sử dụng Flask

```Python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello world!"

if __name__ == '__main__':
    app.run(port=5002, debug=True)

```

4. Thực hiện import flask_restfull
```Python
from flask_restful import Resource, Api
```

Thêm đoạn lệnh này vào:
```Python
api = Api(app)
```

5. Tạo một class là class con của lớp Resource.

```Python
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
```

Khai báo lớp này vào flask

```Python
api.add_resource(HelloWorld, '/')
```

Thực hiện xóa bỏ đoạn code thực hiện `@app.route("/")`

Đến đây, code có thể chạy thử với curl để lấy ra đoạn JSON có nội dung {"hello": "world"}

Có thể truy nhập ngay trực tiếp từ

http://127.0.0.1:5002/ để xem kết quả



## Phần 2: PUT
Tạo ứng dụng todos đơn giản qua Restful

```Python
todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')
```
Thực hiện put 1 bản ghi lại
```
curl http://localhost:5002/todo1 -d "data=Remember the milk" -X PUT
```

Dữ liệu 'Remember the milk' sẽ được lưu vào với khóa  'todo1'

Thực hiện lấy ra 'todo1':
```
curl http://localhost:5002/todo1
```
