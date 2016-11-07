import unittest

from base_test import BaseTest
from pages.buy_ticket_page import BuyTicketPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage


class TestTask(BaseTest):

    def test_task(self):
        count_of_people = 4
        mobile = '+15417543010'
        email = 'someemail@gmail.com'
        ticket_delivery = 'parcel-don-mueang'
        alternative = 'precise'
        comment = 'some text'
        card_number = '4242424242424242'
        name = 'myname'
        expiry = '10/18'
        cvc = '123'
        home_page = HomePage(self.driver)
        home_page.navigate()
        home_page.select_trip('Bangkok - Chiang Mai')
        buy_ticket_page = BuyTicketPage(self.driver)
        buy_ticket_page.buy_ticket()
        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_form(count_of_people, mobile, email, ticket_delivery, alternative,
                                comment, card_number, name, expiry, cvc)

if __name__ == '__main__':
    unittest.main()
