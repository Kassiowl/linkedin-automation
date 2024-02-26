from selenium import webdriver

def start_driver():
    driver = webdriver.Firefox()
    driver.get("https://linkedin.com/")
    
    return driver