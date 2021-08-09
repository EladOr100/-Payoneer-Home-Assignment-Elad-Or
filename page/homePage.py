import configparser

from definitions import CONFIG_FILE


class HomePageSwagger:
    def __init__(self, driver):
        self.driver = driver
        self.get_book_by_id_button = '#operations-Books-get_api_v1_Books__id_>div>span'
        self.get_try_it_out_button = '#operations-Books-get_api_v1_Books__id_ button.btn.try-out__btn'
        self.get_id_text_area = '#operations-Books-get_api_v1_Books__id_ .parameters tr[data-param-name="id"] .parameters-col_description input'
        self.get_execute_button = '#operations-Books-get_api_v1_Books__id_ .execute-wrapper button'
        self.get_response_code_ui = '#operations-Books-get_api_v1_Books__id_ .responses-wrapper .responses-inner .responses-table tbody tr.response > .response-col_status'

        self.post_book_button = '#operations-Books-post_api_v1_Books span.opblock-summary-method'
        self.post_try_it_out_button = '#operations-Books-post_api_v1_Books button.btn.try-out__btn'
        self.post_request_body_json_text_area = '#operations-Books-post_api_v1_Books .opblock-section-request-body .opblock-description-wrapper textarea.body-param__text'
        self.post_execute_button = '#operations-Books-post_api_v1_Books  .execute-wrapper button'
        self.post_get_resonse_code = '#operations-Books-post_api_v1_Books .response .response-col_status'

    # get book by id functions

    def press_get_book_by_id_button(self):
        try:
            self.driver.find_element_by_css_selector(self.get_book_by_id_button).click()
        except:
            print("cant find element{}".format(self.get_book_by_id_button))

    def press_try_it_out_button(self):

        try:
            self.driver.find_element_by_css_selector(self.get_try_it_out_button).click()
        except:
            print("cant find element{}".format(self.get_try_it_out_button))

    def insert_book_id(self, book_id):
        try:
            self.driver.find_element_by_css_selector(self.get_id_text_area).send_keys(book_id)
        except:
            print("cant find element{}".format(self.get_id_text_area))

    def press_execute_button(self):
        try:
            self.driver.find_element_by_css_selector(self.get_execute_button).click()
        except:
            print("cant find element{}".format(self.get_id_text_area))

    def get_response_code(self):
        response_code = None
        try:
            response_code = self.driver.find_element_by_css_selector(self.get_response_code_ui).text
        except:
            print("cant find element{}".format(self.get_response_code_ui))
        return response_code

    # add book functions
    def press_post_book_button(self):
        try:
            self.driver.find_element_by_css_selector(self.post_book_button).click()
        except:
            print("cant find element{}".format(self.post_book_button))

    def press_post_try_it_now_button(self):
        try:
            self.driver.find_element_by_css_selector(self.post_try_it_out_button).click()
        except:
            print("cant find element{}".format(self.post_try_it_out_button))

    def insert_post_request_body(self, request_body):
        try:
            self.driver.find_element_by_css_selector(self.post_request_body_json_text_area).clear()
            self.driver.find_element_by_css_selector(self.post_request_body_json_text_area).send_keys(str(request_body))
        except:
            print("cant find element{}".format(self.post_request_body_json_text_area))

    def press_post_execute_button(self):
        try:
            self.driver.find_element_by_css_selector(self.post_execute_button).click()
        except:
            print("cant find element{}".format(self.post_execute_button))

    def get_response_code_post(self):
        try:
            self.driver.find_element_by_css_selector(self.post_execute_button).click()
        except:
            print("cant find element{}".format(self.post_execute_button))
