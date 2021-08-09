import time

from logic.basicTest import BasicTest
from logic.factoryDriver import WebDriverFactory
from page.homePage import HomePageSwagger


class UiTests(BasicTest):
    def __init__(self, config_parser):
        super().__init__(config_parser)
        # driver init - set the driver from config file by factory design pattern
        self.driver_factory = WebDriverFactory(self.web_driver)
        self.driver = self.driver_factory.getWebDriverInstance()

        self.driver.get(self.home_url)
        self.my_page = HomePageSwagger(self.driver)

    def getBookById(self, book_id):
        self.my_page.press_get_book_by_id_button()
        time.sleep(1)
        self.my_page.press_try_it_out_button()
        time.sleep(1)
        self.my_page.insert_book_id(5)
        time.sleep(1)
        self.my_page.press_execute_button()
        time.sleep(1)
        responce_code = self.my_page.get_response_code()
        assert responce_code == 200


    def addBook(self, book_data_body):

        self.my_page.press_post_book_button()
        self.my_page.press_post_execute_button()
        self.my_page.insert_post_request_body(book_data_body)

    def destructor(self):
        self.driver.close()
        self.driver.quit()
        print("TEST ENDED")
