# Flask-simple-Restful
Create a basic RestFul API with flask

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
