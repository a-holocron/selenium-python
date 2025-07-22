from selenium.webdriver.support.select import Select
from seleniumpagefactory import PageFactory


class HomePage(PageFactory):

    def __init__(self,driver):
        self.driver=driver
        self.timeout = 10
        self.highlight= True

    locators ={
        'News':('XPATH','//a[text()="News"]'),
        'Screener': ('XPATH', '//a[text()="Screener"]'),
        'Maps': ('XPATH', '//a[text()="Maps"]'),
        'Insider': ('XPATH', '//a[text()="Insider"]')
    }

    def open_screener(self):
        self.Screener.click()

    def open_insider(self):
        self.Insider.click()
