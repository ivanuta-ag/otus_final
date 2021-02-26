def test_desktops_page(login_page):
    login_page.wait_for_download()
    login_page.check_open_login_page()
    login_page.check_login_button()
    login_page.check_input_email()
    login_page.check_continue_button()
