from flask import Flask, Blueprint, g
from flask_restful import Api, Resource
from resources.user import User
from resources.post import Post
from resources.tag import Tag
import ConfigParser
import sqlite3

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
config = ConfigParser.ConfigParser()
config.read('site.cfg')

DATABASE = config.get('db', 'database')

def connect_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    g.db = connect_db()

@app.after_request
def after_request(response):
    g.db.close()
    return response

api.add_resource(Post, '/post', '/post/<int:id>')
api.add_resource(User, '/user', '/user/<int:id>')
api.add_resource(Tag, '/tag', '/tag/<string:id>')

app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)


