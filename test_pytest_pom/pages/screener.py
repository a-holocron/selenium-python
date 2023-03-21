from distlib.locators import Page
from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory


class ScreenerPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.highlight = True

    locators = {
        'ticker_input': (By.ID, 'tickersInput'),
        'search_ticker': ('XPATH', '//input[@value=">"]')
    }

    def input_ticker(self, ticker):
        self.ticker_input.send_keys(ticker)

    def search_for_ticker(self, ticker):
        self.ticker_input.send_keys(ticker)
        self.search_ticker.click()
