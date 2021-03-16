from selenium import webdriver 
import unittest 

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox() 

    def tearDown(self):
        self.browser.quit() 

    def test_can_start_a_bqs_and_retrieve_it_later(self):

        self.browser.get('http://localhost:8000')

        self.assertIn('Qrated Bio Samples', self.browser.title)
        self.fail('Finish the test!')