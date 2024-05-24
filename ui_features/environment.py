from selenium import webdriver

def before_all(context):
    context.base_url = "http://www.uitestingplayground.com"

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()  # or use another WebDriver
    context.driver.maximize_window()
    context.base_url = "http://www.uitestingplayground.com"

def after_scenario(context, scenario):
    context.driver.quit()