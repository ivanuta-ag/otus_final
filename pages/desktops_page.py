from .base import BasePage
from locators.locators import DesktopsPageLocators
from selenium.common.exceptions import TimeoutException
import allure


class DesktopsPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.driver = driver

    @allure.step('Wait for download "MainPageLocators.HEART"')
    def wait_for_download(self):
        try:
            self.find_element(locator=DesktopsPageLocators.DESKTOPS)
        except TimeoutException:
            print('Страница не загружена')

    @allure.step('Check open desktops page')
    def check_open_desktops_page(self):
        assert self.find_element(locator=DesktopsPageLocators.DESKTOPS), "Открыта некорректная страница"

    @allure.step('Check count footer blocks')
    def check_count_footer_blocks(self):
        len_footer_blocks = len(self.find_elements(locator=DesktopsPageLocators.FOOTER))
        assert len_footer_blocks == 4, f'Неверное количество элементов меню'

    @allure.step('Check count list group')
    def check_count_list_group(self):
        len_list_group = len(self.find_elements(locator=DesktopsPageLocators.LIST_GROUP))
        assert len_list_group == 10, "Неверное количество элементов в списке"

    @allure.step('Check count_products')
    def check_count_products(self):
        len_products = len(self.find_elements(locator=DesktopsPageLocators.PRODUCTS))
        assert len_products == 12, "Неверное количество продуктов в списке"
