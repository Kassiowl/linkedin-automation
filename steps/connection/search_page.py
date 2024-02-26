from selenium import webdriver
from selenium.webdriver.common.by import By

from repository.get_search_string import get_search_info
def search_page(driver: webdriver, page_number):

    search_info = get_search_info()
    search_string = search_info.search_string

    search_url_with_page = f'https://www.linkedin.com/search/results/people/?keywords={search_string}&page={page_number}'

    driver.get(search_url_with_page)