from random import randint
import random

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    amount_of_seats_xpath = '//*[@id="seats"]'
    mobile_xpath = '//*[@id="contact[mobile]"]'
    email_xpath = '//*[@id="contact[email]"]'
    alternative_xpath = '//*[@id="alternative[srt_alternative]"]'
    comment_xpath = '//*[@id="alternative[comment]"]'
    ticket_delivery_xpath = '//*[@id="delivery[srt_delivery]"]'
    return_ticket_xpath = '//*[@id="return[return_godate]"]'
    card_number_xpath = '//input[@name="number"]'
    name_xpath = '//input[@name="name"]'
    expiry_xpath = '//input[@name="expiry"]'
    cvc_xpath = '//input[@name="cvc"]'
    paypal_button = '//*[@id="omise"]//button'
    success_xpath = '//div[@class="alert alert-success"]'

    def fill_form(self, amount_of_people, mobile, email, ticket_delivery, alternative, comment, card_number,
                  name, expiry, cvc):
        self.select_amount_of_people(amount_of_people)
        self.enter_mobile(mobile)
        self.enter_email(email)
        self.enter_personal_details(amount_of_people)
        self.select_alternative(alternative)
        self.write_comment(comment)
        self.select_ticket_delivery(ticket_delivery)
        self.enter_card_number(card_number)
        self.enter_name(name)
        self.enter_expiry(expiry)
        self.enter_cvc(cvc)
        self.paid()
        self.wait_success()

    def select_amount_of_people(self, amount_of_people):
        if isinstance(amount_of_people, int):
            amount_of_people = str(amount_of_people)
        self.select_value_in_drop_list(self.amount_of_seats_xpath, amount_of_people)

    def enter_mobile(self, mobile):
        self.enter_text_into_field(self.mobile_xpath, mobile)

    def enter_email(self, email):
        self.enter_text_into_field(self.email_xpath, email)

    def enter_personal_details(self, amount_of_people):
        if isinstance(amount_of_people, str):
            amount_of_people = int(amount_of_people)
        for people in range(amount_of_people):
            name_xpath = '//*[@id="passenger[%s][full_name]"]' % people
            passport_xpath = '//*[@id="passenger[%s][id_no]"]' % people
            gender_xpath = '//*[@id="passenger[%s][gender]"]' % people
            seattype_xpath = '//*[@id="passenger[%s][seattype_code]"]' % people
            self.enter_text_into_field(name_xpath, random.choice(['Bob First', 'Alex Second', 'Maria Third']))
            self.enter_text_into_field(passport_xpath, '12345678')
            # self.select_value_in_drop_list(seattype_xpath, random.choice(['lower', 'upper']))
            self.select_value_in_drop_list(gender_xpath, str(randint(0, 2)))

    def select_ticket_delivery(self, ticket_delivery):
        self.select_value_in_drop_list(self.ticket_delivery_xpath, ticket_delivery)

    def select_alternative(self, alternative):
        self.select_value_in_drop_list(self.alternative_xpath, alternative)

    def write_comment(self, comment):
        self.enter_text_into_field(self.comment_xpath, comment)

    def enter_card_number(self, card_number):
        for symbol in card_number:
            self.enter_text_into_field(self.card_number_xpath, symbol)

    def enter_name(self, name):
        self.enter_text_into_field(self.name_xpath, name)

    def enter_expiry(self, expiry):
        for symbol in expiry:
            self.enter_text_into_field(self.expiry_xpath, symbol)

    def enter_cvc(self, cvc):
        self.enter_text_into_field(self.cvc_xpath, cvc)

    def paid(self):
        self.click_on_the_object(self.paypal_button)

    def wait_success(self):
        self.wait_object(self.success_xpath)
