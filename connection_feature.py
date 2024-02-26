
from repository.get_credentials import get_credentials

import time
from repository.get_search_string import get_search_info
from steps.connection.search_page import search_page

from steps.common_steps.login_step import login_step
from steps.connection.send_connection import send_connection
from steps.common_steps.start_driver import start_driver
from util.close_driver import close_driver


credentials = get_credentials()

driver = start_driver()
time.sleep(5)
login_step(driver)
time.sleep(10)

search_info = get_search_info()

until_page = search_info.until_page
current_page = search_info.start_page

while current_page <= until_page:
    search_page(driver, current_page)
    send_connection(driver)
    time.sleep(5)
    current_page+=1


time.sleep(10)
close_driver(driver)