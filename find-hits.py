import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# sets the webdriver to be headless, operating in background
# NOTE: place options=options in driver when uncomment
# options = Options()
# options.headless = True
# options.add_argument('--window-size=1920,1200')

# load in .env 
load_dotenv()

# sets path, search queries, and url
# change to Path from .env after debugging 
driver_path = os.getenv('DRIVER_PATH')
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

QUERIES = ['stem', 'computer', 'science', 'technology', 'python', 'java', 'c++']
url = 'https://www.scholarships.com'

# sets driver, gets url, maximize window (for testing)
driver = webdriver.Chrome(driver_path)
driver.get(url)
driver.maximize_window()

def Login(em, pwd):
    # locates login, clicks login button
    login_element = driver.find_element_by_link_text('Login')
    login_element.click()

    # enter email
    email_element = driver.find_element_by_id('Email')
    email_element.clear()
    email_element.send_keys(em)

    # enter password
    password_element = driver.find_element_by_name('Password')
    password_element.clear()
    password_element.send_keys(pwd)

    # click continue
    continue_button = driver.find_element_by_css_selector('.mdc-button')
    continue_button.click()

Login(email, password)

soup = BeautifulSoup(driver.page_source, 'html.parser')
scholarships = soup.find_all('a', class_='scholarship-matches')

# NOTE: may want to create a function that excludes ad scholarships, which are located under <span>
# should click first scholarship then check for hits then send info if there is a hit, if not
# click arrow to next scholarship and repeat 

# pause to see the result 
# time.sleep(5)




driver.quit()