# This module run the flask web server
# Provides response to the client on REST api requests
# Using the db_connector module in order to store and bring the data provided by client

from flask import Flask, request
from pymysql.err import IntegrityError
from db_connector import add_user, update_user, delete_user, get_user

app = Flask(__name__)


def get_user_from_db(user_id):
    # Function used in GET,DELETE and PUT methods
    # This function is used check if user is already located in the DB
    # It returns the USER_NAME or Error code
    try:
        user_name = get_user(user_id)
        return 0, user_name
    except TypeError as err:
        message = (err.args[0])
        if ("object is not subscriptable" in message):
            return 1, None
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        return 3, None


def get_user_name_from_input_json(input_json):
    # function used in PUT and POST methods
    # getting the json data payload from request
    request_data = input_json
    # treating request_data as a dictionary to get a specific value from key
    user_name = request_data.get('user_name')
    return user_name


# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'POST':

        user_name = get_user_name_from_input_json(request.json)
        try:
            add_user(user_id, user_name)
            return {'status': 'ok', 'user_added': user_name}, 200  # status code
        except IntegrityError as err:
            message = (err.args[1])
            if ("Duplicate entry" in message):
                return {'status': 'error', 'reason': 'id already exists'}, 500  # status code
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return {'status': 'error', 'reason': 'other error'}, 500  # status code

    elif request.method == 'GET':
        response_code, user_name = get_user_from_db(user_id)
        if response_code == 0:
            return {'status': 'ok', 'user_name': user_name}, 200  # status code
        elif response_code == 1:
            return {'status': 'error', 'reason': 'no such id'}, 500  # status code
        else:
            return {'status': 'error', 'reason': 'other error'}, 500  # status code

    elif request.method == 'PUT':

        new_user_name = get_user_name_from_input_json(request.json)
        response_code, user_name = get_user_from_db(user_id)
        if response_code == 0:
            try:
                update_user(user_id, new_user_name)
                return {'status': 'ok', 'user_updated': new_user_name}, 200  # status code
            except Exception as err:
                print(f"Unexpected {err=}, {type(err)=}")
                return {'status': 'error', 'reason': 'other error'}, 500  # status code
        elif response_code == 1:
            return {'status': 'error', 'reason': 'no such id'}, 500  # status code
        else:
            return {'status': 'error', 'reason': 'other error'}, 500  # status code


    elif request.method == 'DELETE':

        response_code, user_name = get_user_from_db(user_id)
        if response_code == 0:
            try:
                delete_user(user_id)
                return {'status': 'ok', 'user_deleted': user_name}, 200  # status code
            except Exception as err:
                print(f"Unexpected {err=}, {type(err)=}")
                return {'status': 'error', 'reason': 'other error'}, 500  # status code
        elif response_code == 1:
            return {'status': 'error', 'reason': 'no such id'}, 500  # status code
        else:
            return {'status': 'error', 'reason': 'other error'}, 500  # status code


app.run(host='127.0.0.1', debug=True, port=5000)
