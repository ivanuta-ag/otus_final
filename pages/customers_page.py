from .base import BasePage
from locators.locators import AdminLocators, CommonPageLocators, CustomersLocators
from selenium.common.exceptions import TimeoutException
import allure
import time


class CustomerPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.driver = driver
        self.driver.implicitly_wait(10)

    @allure.step('Wait for download "AdminLocators.HEART"')
    def wait_for_download(self):
        try:
            self.find_element(locator=AdminLocators.LOGIN_TEXT)
        except TimeoutException:
            print('Страница не загружена')

    @allure.step('Click on button_filter')
    def click_on_button_filter(self):
        self.find_element(locator=CustomersLocators.BUTTON_FILTER).click()

    @allure.step('Input customer name')
    def input_customer_name(self, customer_name):
        inp = self.find_element(locator=CustomersLocators.INPUT_NAME)
        inp.send_keys(customer_name)

    @allure.step('Input email')
    def input_email(self, email):
        inp = self.find_element(locator=CustomersLocators.INPUT_EMAIL)
        inp.send_keys(email)

    @allure.step('Input ip')
    def input_ip(self, ip):
        inp = self.find_element(locator=CustomersLocators.INPUT_IP)
        inp.send_keys(ip)

    @allure.step('Open customers')
    def open_customers(self):
        self.find_element(locator=AdminLocators.LOGIN).click()
        self.is_element_present(*AdminLocators.USER_PROFILE)
        self.find_element(locator=CustomersLocators.MENU_CUSTOMER).click()
        time.sleep(1)
        self.find_element(locator=CustomersLocators.TAB_CUSTOMER).click()

    @allure.step('Should be compare customer name in filters and Customer List')
    def should_be_compare_customer_name(self, customer_name):
        name = self.find_element(locator=CustomersLocators.LIST_CUSTOMER_NAME).text
        assert customer_name in name, f'Expected {customer_name}, got {name}'

    @allure.step('Should be compare e-mail in filters and Customer List')
    def should_be_compare_email(self, email):
        email_actual = self.find_element(locator=CustomersLocators.LIST_EMAIL).text
        assert email in email_actual, f'Expected {email}, got {email_actual}'

    @allure.step('Should be compare ip in filters and Customer List')
    def should_be_compare_ip(self, ip):
        ip_actual = self.find_element(locator=CustomersLocators.LIST_IP).text
        assert ip in ip_actual, f'Expected {ip}, got {ip_actual}'
