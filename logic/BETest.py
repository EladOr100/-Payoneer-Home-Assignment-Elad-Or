import requests

from logic.basicTest import BasicTest


class BETests(BasicTest):
    def __init__(self, config_parser):
        super().__init__(config_parser)

    def addBook(self, book_body):
        headers = {"Accept": "application/json, text/plain, */*"}
        add_book_home_url = 'https://fakerestapi.azurewebsites.net/api/v1/Books'
        response = requests.post(add_book_home_url, data=book_body, headers=headers)
        add_book_flag = self.getBookById(book_body['id'])
        assert add_book_flag is True

    def getBookById(self, book_id):
        response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Books/{}'.format(book_id))
        assert response.status_code == 200
        if response.status_code != 200:
            print("Error")
            return False
        else:
            print("book found")
            return True

    def destructor(self):
        pass
