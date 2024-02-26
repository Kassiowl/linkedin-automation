from dotenv import dotenv_values
from entities.message import Message

MESSAGE_TEXT_PATH = 'static/message.txt'

def get_message() -> Message:
    data = ''
    config = dotenv_values(".env")  
    with open(MESSAGE_TEXT_PATH, "r", encoding="UTF-8") as f:
        raw_text_file = f.read()

    raw_text_file = raw_text_file.rstrip()
    data = raw_text_file.split(config['MESSAGE_SPLIT_PARAGRAPHS'])
    data = [d.replace('\n', ' ') for d in data]
    return Message(config['MESSAGE_TO_WHO'], data)
