from pages.base_page import BasePage


class LoginPage(BasePage):
    scout_panel_xpath = "//h5[contains(text(),'Scouts Panel')]"
    password_xpath ="input[@id='password']"
    remind_password_xpath ="a[contains(text(),'Remind password')]"
    change_language_xpath ="//body[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]"
    login_field_xpath = "//*[@id='login']"
    sign_in_button_xpath = "//body[1]/div[1]/form[1]/div[1]/div[2]/button[1]/span[1]"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
    def type_in_password(self, password):
        self.field_send_keys(self.password_xpath, password)
    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)
    def title_of_page(self):
        assert self.get.page.title(self.login_url) == self.expected_title


