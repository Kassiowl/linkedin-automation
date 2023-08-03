
from repository.get_credentials import get_credentials
from selenium.webdriver.common.by import By

def login_step(driver):
    user_login_element_id = "session_key"
    user_password_element_id = "session_password"

    login_element = driver.find_element(By.ID, user_login_element_id)

    password_element = driver.find_element(By.ID, user_password_element_id)

    login_button_element = driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form[1]/div[2]/button")


    credentials = get_credentials()

    login_element.send_keys(credentials.login)
    password_element.send_keys(credentials.password)
    login_button_element.click()