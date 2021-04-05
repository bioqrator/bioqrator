from selenium import webdriver 
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import unittest 
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time 

MAX_TIME = 10

def wait(fn):
    def modified_fn(*args, **kwargs):
        start_time = time.time()
        while True:
            try:
                return fn(*args, **kwargs)
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_TIME:
                    raise e
                time.sleep(0.5)
    return modified_fn
    

class FunctionalTest(StaticLiveServerTestCase):
    
    @wait
    def wait_for(self, fn):
        return fn()

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

class NewVisitorTest(FunctionalTest):

    def test_can_go_to_submit_page(self):

        self.browser.get('http://localhost:8000/biosamples')
        
        self.browser.find_element_by_id('submit_button').send_keys(Keys.ENTER)

        input_box = self.wait_for(lambda: self.browser.find_element_by_id('id_sample_name'))
        input_box.send_keys("Biosample 1")
        input_box.send_keys(Keys.ENTER)

        detail_sample_name = self.wait_for(lambda: self.browser.find_element_by_id('detail_sample_name'))
        self.assertEqual(detail_sample_name.text, "Biosample 1")

    def test_can_submit_biosample(self):
        
        self.browser.get('http://localhost:8000/biosamples/add')

        input_box = self.browser.find_element_by_id('id_sample_name')

        input_box.send_keys("Biosample 1")
        
        input_box.send_keys(Keys.ENTER)

        sample_name_el = self.wait_for(lambda: self.browser.find_element_by_id('detail_sample_name'))
        sample_name = sample_name_el.text 
        
        self.assertEqual(sample_name, "Biosample 1")

class BiosampleValidationTest(FunctionalTest):

    def test_cannot_submit_empty_sample_name(self):

        self.browser.get('http://localhost:8000/biosamples/add')

        input_box = self.wait_for(lambda: self.browser.find_element_by_id('id_sample_name'))

        input_box.send_keys(Keys.ENTER)

        self.wait_for(lambda: self.browser.find_element_by_css_selector('#id_sample_name:invalid'))


if __name__=="__main__":
    unittest.main()