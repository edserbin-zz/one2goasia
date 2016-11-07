from pages.base_page import BasePage


class HomePage(BasePage):

    def select_trip(self, name_of_trip):
        self.click_on_the_object("//*[contains(text(), '%s')]" % name_of_trip)
