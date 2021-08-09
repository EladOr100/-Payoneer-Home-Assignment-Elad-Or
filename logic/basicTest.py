import configparser

from definitions import CONFIG_FILE


class BasicTest:
    def __init__(self, config_parser):
        self.my_config_parser = config_parser
        self.home_url = self.my_config_parser.get("SITE", "URL")
        self.web_driver = self.my_config_parser.get("DRIVER", "BROWSER")

    def addBook(self, book_id):
        pass

    def getBookById(self, book_id):
        pass
