from flask import g
from flask_restful import Resource
import json

class Post(Resource):
    def query_db(self, query, args=(), one=False):
        cur = g.db.execute(query, args)
        rv = [dict((cur.description[idx][0], value) for idx, value in enumerate(row)) for row in cur.fetchall()] 
        return rv
    def get(self):
        rv = self.query_db("select * from posts")
        return json.dumps(rv)
    def post(self):
        pass
