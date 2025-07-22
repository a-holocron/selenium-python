from distlib.locators import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from seleniumpagefactory import PageFactory


class ScreenerPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.highlight = True

    locators = {
        'ticker_input': (By.ID, 'tickersInput'),
        'search_ticker': ('XPATH', '//input[@value=">"]'),
        'Exchanges': ('ID', 'fs_exch')

    }

    def input_ticker(self, ticker):
        self.ticker_input.send_keys(ticker)

    def search_for_ticker(self, ticker):
        self.ticker_input.send_keys(ticker)
        self.search_ticker.click()

    # Returns a list of all available exchanges in the dropdown
    def get_exchanges(self):
        s = Select(self.Exchanges)
        return s.options
