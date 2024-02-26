from selenium import webdriver

from repository.get_message import get_message

def go_to_send_message_main_page(driver: webdriver):
    message = get_message()
    message_main_page = f'https://www.linkedin.com/search/results/people/?keywords={message.message_to_who}&network=%5B%22F%22%5D&origin=FACETED_SEARCH&sid=%3Bkx'
    driver.get(message_main_page)