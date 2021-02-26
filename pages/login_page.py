from .base import BasePage
from locators.locators import LoginPageLocators, CommonPageLocators
from selenium.common.exceptions import TimeoutException


class LoginPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.driver = driver

    def wait_for_download(self):
        try:
            self.find_element(locator=LoginPageLocators.LOGIN_PAGE)
        except TimeoutException:
            print('Страница не загружена')

    def check_open_login_page(self):
        assert self.find_element(locator=LoginPageLocators.LOGIN_PAGE), "Открыта некорректная страница"

    def check_login_button(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Отсутствует кнопка логина"

    def check_input_email(self):
        assert self.is_element_present(*LoginPageLocators.INPUT_EMAIL), "Отсутствует поле E-Mail Address"

    def check_input_password(self):
        assert self.is_element_present(*CommonPageLocators.INPUT_PASSWORD),"Отсутствует поле Password"

    def check_continue_button(self):
        assert self.is_element_present(*LoginPageLocators.CONTINUE), "Отсутствует кнопка Continue"

