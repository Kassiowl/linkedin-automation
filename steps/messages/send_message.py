import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from repository.get_message import get_message
from selenium.webdriver.common.keys import Keys

def send_message_inside_box(driver: webdriver):
    message = get_message()
    
    time.sleep(2)

    active_element = driver.switch_to.active_element

    for text in message.message_string:
        active_element.send_keys(text)
        active_element.send_keys(Keys.ENTER)
        active_element.send_keys(Keys.ENTER)

    button_xpath = '/html/body/div[5]/div[4]/aside[1]/div[2]/div[1]/div[2]/div/form/footer/div[2]/div[1]/button'
    time.sleep(5)
    button = driver.find_element(By.XPATH, button_xpath)
    button.click()

    time.sleep(2)
    box_element = driver.find_element(By.XPATH, "//div[contains(@class,'msg-overlay-conversation-bubble')]")
    buttons = box_element.find_elements(By.TAG_NAME, "button")
    
    close_button_span = 'Fechar conversa'
    for button in buttons:
        button_span_text = button.find_element(By.TAG_NAME, 'span')
        if close_button_span in button_span_text.text:
            button.click()

    
def send_message(driver: webdriver):
    seconds_to_wait = 5
    driver.implicitly_wait(seconds_to_wait)

    div_class = 'search-results-container'

    div_container_result = driver.find_element(By.CLASS_NAME, div_class)

    people_container_name = './/ul'

    people_list = div_container_result.find_element(By.XPATH, people_container_name)

    buttons = people_list.find_elements(By.XPATH, ".//button")

    button_send_message_span_text = 'Enviar mensagem'
    
    for button in buttons:
        try:
            button_span_text = button.find_element(By.CLASS_NAME, 'artdeco-button__text').text
            if button_send_message_span_text in button_span_text:
                button.click()
                send_message_inside_box(driver)

        except Exception as e:
            print(e)
            continue
