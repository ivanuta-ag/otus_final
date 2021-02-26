from .base import BasePage
from locators.locators import MainPageLocators
from selenium.common.exceptions import TimeoutException
import allure


class MainPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.driver = driver

    @allure.step('Wait for download "MainPageLocators.HEART"')
    def wait_for_download(self):
        try:
            self.find_element(locator=MainPageLocators.HEART)
        except TimeoutException:
            print('Страница не загружена')

    @allure.step('Check wish list')
    def check_wish_list(self):
        assert self.find_element(locator=MainPageLocators.HEART), 'Отсутствует wish list'

    @allure.step('Check len_menu_items')
    def check_len_menu_items(self):
        len_menu_items = len(self.find_elements(locator=MainPageLocators.NAVBAR_1))
        assert len_menu_items == 8, 'Неверное количество элементов меню'

    @allure.step('Check navbar')
    def navbar(self):
        assert self.is_element_present(*MainPageLocators.NAVBAR_2), 'Отсутствует navbar'

    @allure.step('Check logo')
    def check_logo(self):
        assert self.is_element_present(*MainPageLocators.LOGO), 'Отсутствует logo'
