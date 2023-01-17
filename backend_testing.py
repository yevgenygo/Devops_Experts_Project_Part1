import requests
import db_connector

USER_ID = 96
USER_NAME = "test"


def post_user():
    res = requests.post('http://127.0.0.1:5000/users/' + str(USER_ID), json={"user_name": USER_NAME})
    res_data = res.json()
    return res_data, res.status_code


def get_user():
    res = requests.get('http://127.0.0.1:5000/users/' + str(USER_ID))
    res_data = res.json()
    return res_data['user_name'], res.status_code


post_json, post_status = post_user()
if post_status == 200:
    user_name_from_get, get_status = get_user()
    if user_name_from_get == USER_NAME:
        print("Test passed successfully - GET REST method showed the same user name that was sent by POST REST METHOD")
        print("Status of get rest request" + str(get_status))
        print("Direct query for user name from DB: " + str(db_connector.get_user(USER_ID)))
    else:
        print("Status of get rest request" + str(get_status))
else:
    print("POST user failed:" + str(post_json))
