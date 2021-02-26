from .base import BasePage
from locators.locators import AdminLocators, CommonPageLocators
from selenium.common.exceptions import TimeoutException
import allure
import time

class AdminPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.driver = driver

    @allure.step('Wait for download "AdminLocators.HEART"')
    def wait_for_download(self):
        try:
            self.find_element(locator=AdminLocators.LOGIN_TEXT)
        except TimeoutException:
            print('Страница не загружена')

    @allure.step("Check login text")
    def check_login_text(self):
        assert self.find_element(locator=AdminLocators.LOGIN_TEXT), "Некорректный текст с просьбой залогиниться"

    @allure.step("Check input username")
    def check_input_username(self):
        assert self.is_element_present(*AdminLocators.INPUT_USERNAME), "Отсутствует поле ввода логина"

    @allure.step("Check login field")
    def check_login_field(self):
        assert self.is_element_present(*AdminLocators.LOGIN), "Отсутствует поле E-Mail Address"

    @allure.step("Check input password")
    def check_input_password(self):
        assert self.is_element_present(*CommonPageLocators.INPUT_PASSWORD), "Отсутствует поле Password"

    @allure.step("Check help block")
    def check_help_block(self):
        assert self.is_element_present(*AdminLocators.HELP_BLOCK), "Отсутствует help-block"

    @allure.step("Check login")
    def check_login(self):
        self.find_element(locator=AdminLocators.LOGIN).click()
        assert self.is_element_present(*AdminLocators.USER_PROFILE), 'Пользователь не залогинен'

    @allure.step("Check logout")
    def check_logout(self):
        time.sleep(1)
        self.find_element(locator=AdminLocators.LOGOUT).click()
        assert self.is_element_present(*AdminLocators.LOGIN_TEXT), "Не появился текст с просьбой залогиниться"

    @allure.step("Check table responsive")
    def table_responsive(self):
        time.sleep(2)
        self.find_element(locator=AdminLocators.PARENT_COLLAPSE).click()
        self.find_element(locator=AdminLocators.PRODUCTS_CATALOG).click()
        self.is_element_present(*AdminLocators.TABLE_RESPONSIVE), 'Пользователь не залогинен'
