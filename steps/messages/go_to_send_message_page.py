from selenium import webdriver

from repository.get_message import get_message
def go_to_send_message_main_page(driver: webdriver, page: int):
    message = get_message()
    message_main_page = f'https://www.linkedin.com/search/results/people/?keywords={message.message_to_who}&network=%5B%22F%22%5D&origin=GLOBAL_SEARCH_HEADER&page={page}&sid=%2CLg'
    driver.get(message_main_page)