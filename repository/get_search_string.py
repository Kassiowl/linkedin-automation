from dotenv import dotenv_values

from entities.search_string import SearchInfo

def get_search_info() -> SearchInfo:
    config = dotenv_values(".env")  
    return SearchInfo(config['SEARCH_STRING'], int(config['UNTIL_PAGE']), int(config['START_PAGE']))