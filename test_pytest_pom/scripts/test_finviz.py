import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test_pytest_pom.pages.home import HomePage
from test_pytest_pom.pages.screener import ScreenerPage
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("set_up")
class TestFinVizScreener:

    @pytest.mark.order(1)
    def test_finviz_page_loads(self):
        print('page load')
        self.driver.get('https://finviz.com/')
        title = self.driver.title
        assert 'Stock Screener' in title

    @pytest.mark.order(2)
    def test_finviz_screener(self):
        print('screener')
        self.driver.get('https://finviz.com/')
        homepage = HomePage(self.driver)
        homepage.open_screener()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[text()="Dividend Yield"]'))
        )
        print(f'Dividend exist -> {element}')
        screener_page = ScreenerPage(self.driver)
        screener_page.search_for_ticker('AMZN')
    @pytest.mark.order(3)
    def test_finviz_insider(self):
        print('insider')
        self.driver.get('https://finviz.com/')
        homepage = HomePage(self.driver)
        homepage.open_insider()

    @pytest.mark.order(4)
    def test_finviz_screener_exchanges(self):
        expectedExchanges ={'Any','AMEX','NASDAQ','Custom (Elite only)','NYSE'}
        print('screener')
        self.driver.get('https://finviz.com/')
        homepage = HomePage(self.driver)
        homepage.open_screener()
        screenerPage = ScreenerPage(self.driver)
        exchanges = screenerPage.get_exchanges()
        for exchange in exchanges:
            assert exchange.text in expectedExchanges
            print(exchange.text)
