from selenium import webdriver

def start_driver():
    driver = webdriver.Firefox()
    driver.get("https://www.linkedin.com/")
    
    return driver