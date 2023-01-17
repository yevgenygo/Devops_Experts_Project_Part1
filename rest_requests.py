import requests


def post_user(USER_ID, USER_NAME):
    res = requests.post('http://127.0.0.1:5000/users/' + str(USER_ID), json={"user_name": USER_NAME})
    res_data = res.json()
    return res_data, res.status_code


def get_user(USER_ID):
    res = requests.get('http://127.0.0.1:5000/users/' + str(USER_ID))
    res_data = res.json()
    return res_data['user_name'], res.status_code
