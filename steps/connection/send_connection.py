
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def click_button_inside_modal(driver):
    modal_id = 'artdeco-modal-outlet'
    div_modal = driver.find_element(By.ID, modal_id)
    button = div_modal.find_element(By.XPATH, ".//button[@aria-label='Enviar agora']")
    
    button.click()



def send_connection(driver: webdriver):


    seconds_to_wait = 5
    driver.implicitly_wait(seconds_to_wait)

    div_class = 'search-results-container'

    div_container_result = driver.find_element(By.CLASS_NAME, div_class)

    people_container_name = './/ul'

    people_list = div_container_result.find_element(By.XPATH, people_container_name)

    buttons = people_list.find_elements(By.XPATH, ".//button")

    button_connect_span_text = 'Conectar'
    
    for button in buttons:
        try:
            button_span_text = button.find_element(By.CLASS_NAME, 'artdeco-button__text').text
            if button_connect_span_text in button_span_text:
                button.click()
                click_button_inside_modal(driver)
        except Exception as e:
            print(e)
            continue

