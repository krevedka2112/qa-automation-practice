def test_login_success(login_page, config):
    """Проверяем логин на сайте с валидными username и password"""

    login_page.navigate_to(config["web"]["login_url"])
    login_page.login(config["username"], config["password"])

    assert login_page.flash_message.is_visible()
    assert "You logged into a secure area!" in login_page.flash_message.text_content()


def test_login_fail(login_page, config):
    """Проверяем логин на сайте с невалидными username и password"""

    login_page.navigate_to(config["web"]["login_url"])
    login_page.login("invalid_user", "wrong_password")

    assert login_page.flash_message.is_visible()
    assert "Your username is invalid!" in login_page.flash_message.text_content()
