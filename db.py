from flask import g

class DBI():
    def query_db(self, query, args=(), one=False):
        cur = g.db.execute(query, args)
        rv = [dict((cur.description[idx][0], value) for idx, value in enumerate(row)) for row in cur.fetchall()] 
        return rv
