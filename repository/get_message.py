from dotenv import dotenv_values
from entities.message import Message

MESSAGE_TEXT_PATH = 'static/message.txt'

def get_message() -> Message:
    data = ''
    config = dotenv_values(".env")  
    with open(MESSAGE_TEXT_PATH, "r", encoding="UTF-8") as f:
        data = f.read()
    return Message(config['MESSAGE_TO_WHO'], data)
