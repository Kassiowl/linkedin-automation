
import time
from repository.get_message import get_message
from steps.common_steps.login_step import login_step
from steps.common_steps.start_driver import start_driver
from steps.messages.go_to_send_message_page import go_to_send_message_main_page
from steps.messages.send_message import send_message




message = get_message()

print("Message")
print(message.message_string)

driver = start_driver()
time.sleep(5)
login_step(driver)
time.sleep(5)
go_to_send_message_main_page(driver)
time.sleep(10)
send_message(driver)
