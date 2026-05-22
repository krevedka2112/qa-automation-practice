from playwright.sync_api import Page
from utils.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.submit_button = page.locator("button[type='submit']")
        self.flash_message = page.locator("#flash")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)

        self.submit_button.click()
