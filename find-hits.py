import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# sets the webdriver to be headless, operating in background
# can't do this for this project, keeping for info later
# NOTE: place options=options in driver when uncomment
# options = Options()
# options.headless = True
# options.add_argument('--winddow-size=1920,1200')

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

# locates login, clicks login button
login_element = driver.find_element_by_link_text('Login')
login_element.click()

email_element = driver.find_element_by_id('Email')
email_element.clear()
# change to email from .env after debugging
email_element.send_keys(email)

password_element = driver.find_element_by_name('Password')
password_element.clear()
# change to password from .env after debugging
password_element.send_keys(password)

# pause to see the result 
time.sleep(5)

# soup = BeautifulSoup(driver.page_source, 'html.parser')



driver.quit()