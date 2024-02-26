
import time
from repository.get_message import get_message
from repository.get_search_string import get_search_info
from steps.common_steps.login_step import login_step
from steps.common_steps.start_driver import start_driver
from steps.messages.go_to_send_message_page import go_to_send_message_main_page
from steps.messages.send_message import send_message




message = get_message()

print("Message")
print(message.message_string)
search_info = get_search_info()

until_page = search_info.until_page
current_page = search_info.start_page

driver = start_driver()
login_step(driver)
time.sleep(20)
while current_page <= until_page:
    time.sleep(5)
    go_to_send_message_main_page(driver, current_page)
    time.sleep(5)
    send_message(driver)
    current_page+=1
