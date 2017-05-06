from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from find_your_cab.views import callLogInPage
from find_your_cab.models import CabUser, CabDriver, DriverHistory

class LogInPageTest(TestCase):

    def test_use_login_page(self):
         response = self.client.get('/')
         self.assertTemplateUsed(response, 'find_your_cab/login.html')

    def test_can_save_a_POST_request(self):
        self.client.post('/', data={'name': 'สมศรี', 'password' : '1100'})

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'name': 'สมศรี', 'password' : '1100'})
        print("?????")
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['location'], 'http://127.0.0.1:8000/homepage/')

    def test_insert_driver(self):
        self.client.post('/homepage/', data={'name_driv': 'สมหมาย'})      

    def test_rate_driver(self):
        self.client.post('/rate/', data={'point': '5'})
'''
class SignInPage(TestCase):
    
    def test_rate_driver(self):
         response = self.client.get('/')
         self.assertTemplateUsed(response, 'find_your_cab/signin.html')   
'''
