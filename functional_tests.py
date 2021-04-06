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
        pass

class BiosampleValidationTest(FunctionalTest):

    FIELDS = {'sample_name': "SM486AYH",
            'organism': "Human", 
            'biosample': "HeLa", 
            'condition': "WT", 
            'treatment': "hsa-miR", 
            'treatment_time': "24hr",
            'treatment_conc': "100nM", 
            'target': "AARS", 
            'assay': "mRNA-seq", 
            'layout': "1x51", 
            'platform': "HiSeq",}

    REQUIRED_FIELDS = ['sample_name', 'organism', 'biosample']

    def populate_field(self, field, value):
        
        input_box = self.wait_for(lambda: self.browser.find_element_by_id(f'id_{field}'))
        
        input_box.send_keys(value)

    def clear_field(self, field):

        input_box = self.wait_for(lambda: self.browser.find_element_by_id(f'id_{field}'))

        input_box.clear()

    def populate_all_fields(self):

        for field, val in self.FIELDS.items():
            self.populate_field(field, val)

    def test_can_submit_biosample(self):

        self.browser.get('http://localhost:8000/biosamples/add')

        self.populate_all_fields()
        save_button = self.browser.find_element_by_id('save_button')
        save_button.send_keys(Keys.ENTER)

        for field, value in self.FIELDS.items():
            li = self.wait_for(lambda: self.browser.find_element_by_id(f'li_{field}'))
            self.assertEqual(li.text.split(':')[-1].strip(), value)

    def check_cannot_submit_with_empty_(self, field):

        self.browser.get('http://localhost:8000/biosamples/add')

        self.populate_all_fields()
        self.clear_field(field)

        save_button = self.browser.find_element_by_id('save_button')
        save_button.send_keys(Keys.ENTER)

        self.wait_for(lambda: self.browser.find_element_by_css_selector(f'#id_{field}:invalid'))

    def test_cannot_submit_with_empty_sample_name(self):
        
        self.check_cannot_submit_with_empty_('sample_name')

    def test_cannot_submit_if_required_fields_are_empty(self):
        
        for field in self.REQUIRED_FIELDS:
            self.check_cannot_submit_with_empty_(field)

    def check_can_submit_with_empty_(self, field):

        self.browser.get('http://localhost:8000/biosamples/add')

        self.populate_all_fields()
        self.clear_field(field)

        save_button = self.browser.find_element_by_id('save_button')
        save_button.send_keys(Keys.ENTER)

        for key, value in self.FIELDS.items():
            li = self.wait_for(lambda: self.browser.find_element_by_id(f'li_{key}'))
            if key != field: 
                self.assertEqual(li.text.split(':')[-1].strip(), value)

    def test_can_submit_with_nonrequired_fields_are_empty(self):
        
        for field in self.FIELDS:
            if field not in self.REQUIRED_FIELDS:
                self.check_can_submit_with_empty_(field)
                
                time.sleep(3)


if __name__=="__main__":
    unittest.main()