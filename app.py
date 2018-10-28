from flask import Flask , request , jsonify
from flask_restful import Resource  , Api
from flask_jwt import JWT , jwt_required
from dbConnection import connection
from authenticate import authenticatea
from security import authenticate

app = Flask(__name__)
app.secret_key = "vivek"
api = Api(app)

c, con = connection()

@app.route('/login' , methods = ['POST'])
def authenticate():
    return authenticatea(request.get_json())


app.run(port = 5000 , debug = True)