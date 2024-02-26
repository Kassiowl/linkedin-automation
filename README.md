# Linkedin Automation


> This is a linkedin connection automation made with selenium, it login and sends connection requests according to the user configuration

### RoadMap

- [x] Connection Request Automation
- [x] Send Message Automation
- [ ] Send Resume(Curriculum) automation


## Setup

1. Install Python3
2. Run ``` pip install -r requirements```
3. Config .env file according to your needs and credentials
4. Config the text file in static/message.txt according to what messade you want to send
4. If you don't have Firefox Installed but have chrome, go to steps/start_driver.py and changes 
``` driver = webdriver.Firefox()``` to ```driver = webdriver.Chrome()``` 
5. Run ```python connection_feature.py``` if you want to send connections or ```python message_feature.py``` if you want to send messages 
