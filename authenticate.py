from flask import Flask , request , jsonify
from dbConnection import connection
c, con = connection()

def authenticatea(data):
    #data = request.get_json()
    userName = data.get('userName' , None)
    password = data.get('password' , None)
    if userName :
        c.execute("SELECT * FROM `users` WHERE userName = %s" , [userName,])
        user = c.fetchall()
        if not user:
             return jsonify({"data" : None , "status" : 401 , "message" : "userName not found"})

        print(user[0].get('password', None))

        if password and password == user[0].get('password', None):
             return jsonify({"data" : user[0] , "status" : 200 , "message" : "Login successful"})
        else:
            return jsonify({'error' : 'Please check your password', "status" : 401})
    else:
        return jsonify({'error' : 'userName is required', "status" : 401})