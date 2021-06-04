"""users test"""

from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
import uuid
from time import sleep
# Create your tests here.

class HostTest(LiveServerTestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='users/../chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
  
    
    def test_login(self):
        driver = self.driver    
        driver.get('http://127.0.0.1:8000/')
        assert 'Instagram' in driver.title
        driver = self.driver
        
        login_field = driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/input')
        login_field.clear()
        login_input = uuid.uuid4().hex.upper()[0:6]
        login_field.send_keys(login_input)
        
        password_field = driver.find_element_by_xpath('/html/body/div/div/div/form/div[2]/input')
        password_field.clear()
        password_input = uuid.uuid4().hex.upper()[0:6]
        password_field.send_keys(password_input)
    
        login_botton = driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/button')
        login_botton.click()
        
        
    def tearDown(self):
        self.driver.close()
        
       
       
  