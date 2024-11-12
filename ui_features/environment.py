from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    context.base_url = "http://www.uitestingplayground.com"

def before_scenario(context, scenario):
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920x1080")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.base_url = "http://www.uitestingplayground.com"

def after_scenario(context, scenario):
    context.driver.quit()
