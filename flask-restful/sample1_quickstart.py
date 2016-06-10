#http://flask-restful-cn.readthedocs.io/en/0.3.4/quickstart.html

from flask import Flask
from flask_restful import Resource, Api

# sudo python3 -m pip install flask-restful 

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)