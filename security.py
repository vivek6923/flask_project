from werkzeug.security import safe_str_cmp
from dbConnection import connection

c, con = connection()

def authenticatea(username , password):
    c.execute("SELECT * FROM `users` WHERE userName = %s" , [username,])
    user = c.fetchall()
    print(user)
    return "Done"