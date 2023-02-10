from selenium.webdriver.common.by import By


class SearchResultPageLocators:

    FIRST_RESULT = (By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]')
    SEARCH_QUERY_FROM_RESULTS_PAGE = '//*[@id="search"]/span/div/h1/div/div[1]/div/div/span[3]'
    RESULTS_HEADER = '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[1]/div/span/div/div/span'
    BACK_TO_RESULTS_LINK = '//*[@id="breadcrumb-back-link"]'