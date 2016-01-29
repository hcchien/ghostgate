import sqlite3
from flask import g

DATABASE = '/Users/hcchien/ghostgate/ghost-dev.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db
