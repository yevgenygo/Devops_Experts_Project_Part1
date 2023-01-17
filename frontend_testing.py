# Test if user exists using selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# when testing directly from the script replace none with th real user_id you want to test
user_id = 500


def frontend_test(user_id):
    driver = webdriver.Chrome(service=Service("C:\temp\chromedriver.exe"))

    driver.get('http://127.0.0.1:5001/users/get_user_name/' + str(user_id))
    user = driver.find_element(By.ID, "user")
    user_name = user.text
    driver.quit()
    return (user_name)


try:
    user_name = frontend_test(str(user_id))
    print(user_name)
except:
    print("Getting error while trying to retrieve user with ID " + str(user_id))
