from flask import Flask, Blueprint
from flask_restful import Api, Resource
from resources.user import User
from resources.post import Post
from resources.tag import Tag

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Post, '/post', '/post/<int:id>')
api.add_resource(User, '/user', '/user/<string:id>')
api.add_resource(Tag, '/tag', '/tag/<string:id>')

app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)

