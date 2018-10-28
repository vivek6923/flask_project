import MySQLdb
from MySQLdb.cursors import DictCursor

def connection():
    conn = MySQLdb.connect(
    cursorclass=DictCursor,
    host = "localhost",
    user = "root",
    # passwd = "testpassword",
    db = "myapp"
    )
    c = conn.cursor()
    return c, conn