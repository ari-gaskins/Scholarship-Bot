import os
import smtplib
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# sets the webdriver to be headless, operating in background
# NOTE: place options=options in driver when uncomment
options = Options()
options.headless = True
options.add_argument('--window-size=1920,1200')

# load in .env 
load_dotenv()

# sets path, search queries, and url
# change to Path from .env after debugging 
driver_path = os.getenv('DRIVER_PATH')
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')
raspberry = os.getenv('RASPBERRY_EMAIL')

QUERIES = ['stem', 'computer', 'science', 'technology', 'python', 'java', 'c++']
url = 'https://www.scholarships.com'

# sets the gmail server
gmail = smtplib.SMTP('smtp.gmail.com', 587)

# sets driver, gets url, maximize window (for testing)
driver = webdriver.Chrome(driver_path, options=options)
driver.get(url)
# driver.maximize_window()

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
# scholarships = soup.find_all('a', 'scholarship-matches')
primitive_matches = soup.find_all('div', 'scholarship-match-header-title')
# NOTE: may want to create a function that excludes ad scholarships, which are located under <span>
# should click first scholarship then check for hits then send info if there is a hit, if not
# click arrow to next scholarship and repeat 
# need to first find a card's data-award-id, then find element by id of scholarship-match-card- + data-award-id


def email_configurations(titles, server, em, pwd): 
    # start and log into email
    server.startls()
    server.login(em, pwd)

    # iterates through matches titles,  starts at 4 to ignore ads,
    # add num_ads in refactoring
    for i in range(4, len(titles)):
        server.sendmail(titles[i].text)
    # exit server    
    server.quit()


driver.quit()