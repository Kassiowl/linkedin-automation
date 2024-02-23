# Linkedin Automation


> This is a linkedin connection automation made with selenium, it login and sends connection requests according to the user configuration

### RoadMap

- [x] Connection Request Automation
- [ ] Send Message Automation
- [ ] Send Resume(Curriculum) automation


## Setup

1. Install Python3
2. Run ``` pip install -r requirements```
3. Config .env file according to your needs and credentials
4. If you don't have Firefox Installed but have chrome, go to steps/start_driver.py and changes 
``` driver = webdriver.Firefox()``` to ```driver = webdriver.Chrome()``` 
5. Run ```python main.py```
