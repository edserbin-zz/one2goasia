from pages.base_page import BasePage


class BuyTicketPage(BasePage):

    one_of_buy_buttons_xpath = '//span[@class="buy-button-text"]'
    check_out_button_xpath = "//*[contains(text(), 'Checkout! ')]"

    def buy_ticket(self):
        self.click_on_the_object(self.one_of_buy_buttons_xpath)
        self.driver.switch_to_active_element()
        self.click_on_the_object(self.check_out_button_xpath)
