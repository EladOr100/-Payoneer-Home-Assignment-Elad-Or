import configparser
from datetime import datetime
import logging
import unittest
from definitions import CONFIG_FILE
from logic import UITest
from logic.BETest import BETests
from logic.UITest import UiTests
from logic.factoryDriver import WebDriverFactory


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("TEST START")

        # config init - get params from config file
        cls.my_config_parser = configparser.ConfigParser()
        cls.my_config_parser.read(CONFIG_FILE)
        cls.test_obj = cls.createMyTestObj()

    @classmethod
    def createMyTestObj(cls):
        # set my_test_obj to UI or BE tests
        my_test_obj = None
        test_type = cls.my_config_parser.get('TEST_INFO', 'TEST_TYPE')
        if test_type == 'UI':
            my_test_obj = UiTests(cls.my_config_parser)
        elif test_type == 'BE':
            my_test_obj = BETests(cls.my_config_parser)
        if my_test_obj is None:
            print("something went wrong. check test TYPE in config file")
        return my_test_obj

    def test_get_book_validation(self):
        print('test_get_book_validation start')
        self.test_obj.getBookById(2)

    def test_add_book_validation(self):
        book_data_body = {
            "id": 0,
            "title": "string",
            "description": "string",
            "pageCount": 0,
            "excerpt": "string",
            "publishDate": "2021-08-09T18:41:33.850Z"
        }
        print('test_add_book_validation start')
        self.test_obj.addBook(book_data_body)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.test_obj.destructor()
        print("TEST END")


if __name__ == '__main__':
    unittest.main()
