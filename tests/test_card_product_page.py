def test_card_product(card_product_page):
    card_product_page.wait_for_download()
    card_product_page.check_card_product()
    card_product_page.check_product_image()
    card_product_page.check_input_quantity_form()
    card_product_page.check_cart()
    card_product_page.check_button_cart()
