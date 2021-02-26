import pytest


@pytest.mark.parametrize("customer_name", ['1234asd', 'Alcatel'])
def test_filters_by_customer_name_field(customer_page, customer_name):
    customer_page.wait_for_download()
    customer_page.open_customers()
    customer_page.input_customer_name(customer_name)
    customer_page.click_on_button_filter()
    customer_page.should_be_compare_customer_name(customer_name)


@pytest.mark.parametrize("email", ['neona@gmail.com', 'ana-maria@yahoo.com'])
def test_filters_by_email_field(customer_page, email):
    customer_page.wait_for_download()
    customer_page.open_customers()
    customer_page.input_email(email)
    customer_page.click_on_button_filter()
    customer_page.should_be_compare_email(email)


@pytest.mark.parametrize("ip", ['141.101.98.110', '162.158.118.148'])
def test_filters_by_ip_field(customer_page, ip):
    customer_page.wait_for_download()
    customer_page.open_customers()
    customer_page.input_ip(ip)
    customer_page.click_on_button_filter()
    customer_page.should_be_compare_ip(ip)
