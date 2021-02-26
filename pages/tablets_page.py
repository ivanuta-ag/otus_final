from .base import BasePage
from locators.locators import TabletsLocators, CommonPageLocators
from selenium.common.exceptions import TimeoutException


class TabletsPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.driver = driver

    def wait_for_download(self):
        try:
            self.find_element(locator=TabletsLocators.TABLETS)
        except TimeoutException:
            print('Страница не загружена')

    def check_tablets(self):
        assert self.is_element_present(*TabletsLocators.TABLETS), 'Некорректное название вкладки'

    def check_goods(self):
        assert self.is_element_present(*TabletsLocators.GOODS), 'Во вкладке нет товаров'

    def check_button_add_to_cart(self):
        assert self.is_element_present(*TabletsLocators.ADD_TO_CART), 'Кнопка Add to Cart отсутствует'

    def check_product_compare(self):
        assert self.is_element_present(*TabletsLocators.PRODUCT_COMPARE), 'Отсутствует Product Compare'
