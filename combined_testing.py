import db_connector
from rest_requests import get_user,post_user
from frontend_testing import frontend_test

USER_ID =12
USER_NAME = "test"

post_json, post_status = post_user(USER_ID,USER_NAME)
if post_status == 200:
    user_name_from_get, get_status = get_user(USER_ID)
    if user_name_from_get == USER_NAME:
        print("Test passed successfully - GET REST method showed the same user name that was sent by POST REST METHOD")
        print("Status of get rest request" + str(get_status))
        print("Direct query for user name from DB: " + str(db_connector.get_user(USER_ID)))
        user_name_sel = frontend_test(str(USER_ID))
        print("Username retrieved via selenium: " + str(user_name_sel))
    else:
        print("Status of get rest request" + str(get_status))
else:
    print("status of post rest request:" + str(post_json))
