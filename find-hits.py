from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# sets the webdriver to be headless, operating in background
# NOTE: place options=options in driver when uncomment
# options = Options()
# options.headless = True
# options.add_argument('--winddow-size=1920,1200')

# sets path, search queries, and url
DRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
QUERIES = ['stem', 'computer', 'science', 'technology', 'python', 'java', 'c++']
url = 'https://www.scholarships.com'

# sets driver, gets url, maximize window (for testing)
driver = webdriver.Chrome(DRIVER_PATH)
driver.get(url)
driver.maximize_window()

# locates login, clicks login button
login_element = driver.find_element_by_link_text('Login')
login_element.click()

email_element = driver.find_element_by_id('Email')


# soup = BeautifulSoup(driver.page_source, 'html.parser')



driver.quit()