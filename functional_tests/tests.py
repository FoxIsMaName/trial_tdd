from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self): #
        #มานีได้ยินเกี่ยวกับแอพนี้จึงลองเปิดขึ้นมาดู
        self.browser.get('http://localhost:8000')
        #เธอเปิดมาเจอหน้า log in
        self.assertIn('log in', self.browser.title) #
        header_1 = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Taxi', header_1) #
        header_2 = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Log In',header_2)

        #เธอใส่ชื่อและรหัส
        name_insert = self.browser.find_element_by_id('name_id')
        name_insert.send_keys('มานี')
        password_insert = self.browser.find_element_by_id('password_id')
        password_insert.send_keys("1035")
        password_insert.send_keys(Keys.ENTER)
        time.sleep(1)

        #เธอพิมพ์หาชื่อ สมหมาย
        driv_insert = self.browser.find_element_by_id('name_driv')
        driv_insert.send_keys('สมหมาย')
        driv_insert.send_keys(Keys.ENTER)
        time.sleep(1)

        #เธอให้คะแนนสมหมาย 4 ดาว
        point_insert = self.browser.find_element_by_id('four')
        point_insert.send_keys(Keys.ENTER)
        time.sleep(1) 

        #เธอกดกลับไปที่หน้า log in
        backHome = self.browser.find_element_by_id('back_home')
        backHome.send_keys(Keys.ENTER)
        time.sleep(1)

        #Don goes to the sign in page
        sign_in = self.browser.find_element_by_id('sign_in')
        sign_in.send_keys(Keys.ENTER)
        time.sleep(1)

        #He insert his name and password
        name_insert = self.browser.find_element_by_id('name_id')
        name_insert.send_keys('Don')
        password_insert = self.browser.find_element_by_id('password_id')
        password_insert.send_keys("1006")
        password_insert.send_keys(Keys.ENTER)        
        time.sleep(1)

        #He click back to the login page
        backHome = self.browser.find_element_by_id('back_home')
        backHome.send_keys(Keys.ENTER)
        time.sleep(1)        

        self.fail('Finish the test!')

    def findid_and_enterinput(self,id_in,text):
        thisbox = self.browser.find_element_by_id(id_in)
        thisbox.send_keys(text)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
