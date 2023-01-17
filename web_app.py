# WEB to the DB that return user_mane in HTML format
from flask import Flask
from db_connector import get_user

app = Flask(__name__)


@app.route("/users/get_user_name/<user_id>")
def get_user_name(user_id):
    user_name = get_user(user_id)
    if not user_name:
        return "<H1 id='error'>""no such user:" + user_id + "</H1>"
    else:
        return "<H1 id='user'>" + user_name + "</H1>"


app.run(host='127.0.0.1', debug=True, port=5001)
