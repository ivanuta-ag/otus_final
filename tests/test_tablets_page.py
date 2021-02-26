def test_tablets_page(tablets_page):
    tablets_page.wait_for_download()
    tablets_page.check_tablets()
    tablets_page.check_goods()
    tablets_page.check_button_add_to_cart()
    tablets_page.check_cart()
    tablets_page.check_product_compare()
