def test_desktops_page(desktops_page):
    desktops_page.wait_for_download()
    desktops_page.check_open_desktops_page()
    desktops_page.check_count_footer_blocks()
    desktops_page.check_count_list_group()
    desktops_page.check_count_products()
    desktops_page.check_cart()
