from .base import BasePage
from locators.locators import CardProductPageLocators
from selenium.common.exceptions import TimeoutException
import allure


class CardProductPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.driver = driver

    @allure.step('Wait for download "CardProductPageLocators.CARD_PRODUCT"')
    def wait_for_download(self):
        try:
            self.find_element(locator=CardProductPageLocators.CARD_PRODUCT)
        except TimeoutException:
            print('Страница не загружена')

    @allure.step('Check card product')
    def check_card_product(self):
        self.find_element(locator=CardProductPageLocators.CARD_PRODUCT), "Открыта некорректная страница"

    @allure.step('Check product image')
    def check_product_image(self):
        self.is_element_present(*CardProductPageLocators.PRODUCT_IMAGE), "Отсутствует изображение товара"

    @allure.step('Check input quantity form')
    def check_input_quantity_form(self):
        assert self.is_element_present(
            *CardProductPageLocators.INPUT_QUANTITY), "Отсутствует форма добавления количества товаров"

    @allure.step('Check button cart')
    def check_button_cart(self):
        assert self.is_element_present(*CardProductPageLocators.BUTTON_CART), "Отсутствует кнопка добавления в корзину"
