from entities.credentials import Credentials
from dotenv import dotenv_values

def get_credentials() -> Credentials:
    config = dotenv_values(".env")  
    return Credentials(config['LINKEDIN_LOGIN'], config['LINKEDIN_PASSWORD'])