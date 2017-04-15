from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

def test_can_start_a_list_and_retrieve_it_later(self): #
    # Edith has heard about a cool new online to-do app. She goes
    # to check out its homepage
    self.browser.get('http://localhost:8000')
    # She notices the page title and header mention to-do lists
    self.assertIn('find your cab', self.browser.title) #
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Let find your cab', header) #
    self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
