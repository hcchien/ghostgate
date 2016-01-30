from db import DBI
from flask_restful import Resource
import json

class model_resource(Resource):
    def __init__(self):
        self.dbi = DBI()
        pass
    def get(self, id = ''):
        if (id != ''):
            rv = self.dbi.query_db("select * from " + self._table + " where id = ?", [id])
        else:
            rv = self.dbi.query_db("select * from " + self._table)
        return json.dumps(rv)
    def post(self):
        pass

