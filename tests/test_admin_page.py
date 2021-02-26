def test_admin_page(admin_page):
    admin_page.wait_for_download()
    admin_page.check_login_text()
    admin_page.check_input_username()
    admin_page.check_input_password()
    admin_page.check_login_field()
    admin_page.check_help_block()


def test_login_admin_page(admin_page):
    admin_page.check_login()
    admin_page.check_logout()


def test_table_with_goods(admin_page):
    admin_page.check_login()
    admin_page.table_responsive()
