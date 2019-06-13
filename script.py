from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

###########################################################

# enter the link to the website you want to automate login.
website_link = "<link>"
# enter your login username
username1 = "<username>"
# enter your login password
password1 = "<password>"

###########################################################

# enter the element for username input field
element_for_username = "username"
# enter the element for password input field
element_for_password = "password"
# enter the element for submit button
element_for_submit = "loginbutton"

###########################################################
browser = webdriver.Firefox()  # for macOS users[for others use chrome vis chromedriver]
browser.get((website_link))

try:
    username = browser.find_element_by_name(element_for_username)
    username.send_keys(username1)
    password = browser.find_element_by_name(element_for_password)
    password.send_keys(password1)
    signInButton = browser.find_element_by_id(element_for_submit)
    signInButton.click()

    #### to quit the browser uncomment the following lines ####
    time.sleep(3)
    browser.quit()
    time.sleep(1)
    browserExe = "Firefox"
    os.system("pkill "+browserExe)
except Exception:
    # This exception occurs if the element are not found in the webpage.
    print ("Some error occured :(")

    #### to quit the browser uncomment the following lines ####
    # browser.quit()
    # browserExe = "Safari"
# os.system("pkill "+browserExe)
