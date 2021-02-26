from selenium.webdriver.common.by import By


class CommonPageLocators():
    # SWIPER = (By.XPATH, '(//*[@class = "swiper-viewport"])[2]/div/div/div')
    CART = (By.XPATH, '//*[@id= "cart"]')
    INPUT_PASSWORD = (By.XPATH, '//*[@id = "input-password"]')


class MainPageLocators:
    HEART = (By.XPATH, '//*[@class = "fa fa-heart"]')
    LOGO = (By.XPATH, '//*[@id = "logo"]')
    NAVBAR_1 = (By.XPATH, '//*[@class = "nav navbar-nav"]/li')
    NAVBAR_2 = (By.XPATH, '//*[@class = "collapse navbar-collapse navbar-ex1-collapse"]')


class LoginPageLocators:
    INPUT_EMAIL = (By.XPATH, '//*[@id = "input-email"]')
    LOGIN_PAGE = (By.XPATH, '//*[@class = "breadcrumb"]//*[text() = "Login"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@value = "Login"]')
    CONTINUE = (By.XPATH, '//*[@class = "btn btn-primary" and text() = "Continue"]')


class DesktopsPageLocators:
    DESKTOPS = (By.XPATH, '//*[@class = "breadcrumb"]//*[text() = "Desktops"]')
    FOOTER = (By.XPATH, '//footer//ul')
    LIST_GROUP = (By.XPATH, '//*[@class = "list-group"]/a')
    PRODUCTS = (By.XPATH, '//*[@class = "product-thumb"]')


class CardProductPageLocators:
    CARD_PRODUCT = (By.XPATH, '//*[@class = "breadcrumb"]//li[3]')
    PRODUCT_IMAGE = (By.XPATH, '//*[@class = "thumbnails"]/li')
    INPUT_QUANTITY = (By.XPATH, '//*[@id = "input-quantity"]')
    BUTTON_CART = (By.XPATH, '//*[@id = "button-cart"]')


class AdminLocators:
    LOGIN_TEXT = (By.XPATH, '//*[text() = " Please enter your login details."]')
    INPUT_USERNAME = (By.XPATH, '//*[@id = "input-username"]')
    LOGIN = (By.XPATH, '//*[@class= "btn btn-primary"]')
    HELP_BLOCK = (By.XPATH, '//*[@class= "help-block"]')
    USER_PROFILE = (By.XPATH, '//*[@id = "user-profile"]')
    LOGOUT = (By.XPATH, '//*[@class = "fa fa-sign-out"]')
    PARENT_COLLAPSE = (By.XPATH, '//*[@class = "parent collapsed"]')
    PRODUCTS_CATALOG = (By.XPATH, '//*[@id= "collapse1"]/li[2]')
    TABLE_RESPONSIVE = (By.XPATH, '//*[@class = "table-responsive"]')


class TabletsLocators:
    TABLETS = (By.XPATH, '//*[text() = "Tablets"]')
    GOODS = (By.XPATH, '//*[@class = "product-thumb"]/div[@class = "image"]')
    ADD_TO_CART = (By.XPATH, '//button//*[text() = "Add to Cart"]')
    PRODUCT_COMPARE = (By.XPATH, '//*[@id = "compare-total"]')


class CustomersLocators:
    BUTTON_FILTER = (By.XPATH, '//*[@id = "button-filter"]')
    INPUT_EMAIL = (By.XPATH, '//*[@id = "input-email"]')
    INPUT_NAME = (By.XPATH, '//*[@id= "input-name"]')
    INPUT_IP = (By.XPATH, '//*[@id= "input-ip"]')
    LIST_CUSTOMER_NAME = (By.XPATH, '((//*[@class = "table table-bordered table-hover"]//tr)[2]/td)[2]')
    LIST_EMAIL = (By.XPATH, '((//*[@class = "table table-bordered table-hover"]//tr)[2]/td)[3]')
    LIST_IP = (By.XPATH, '((//*[@class = "table table-bordered table-hover"]//tr)[2]/td)[6]')
    MENU_CUSTOMER = (By.XPATH, '//*[@id= "menu-customer"]')
    TAB_CUSTOMER = (By.XPATH, '//*[@id= "menu-customer"]/ul//a')
