import os
import unittest
from datetime import date
from dotenv import load_dotenv

from selenium import webdriver

from UTILITIES.log import Log
from UTILITIES.utilities import Utilities
from Pages.base_page import BasePage
from Locators.locators import PageLocators

load_dotenv('.env.test')


class TestAP(unittest.TestCase, BasePage):

    def setUp(self):
        BasePage.__init__(self, webdriver.Chrome())
        self.locator = PageLocators()
        # UTIL
        self.util = Utilities('D:/PythonRepos/SeleniumDDTPython/Pages/DATA/DATA.json')

        # INIT LOGGER
        logger_file = "D:/PythonRepos/SeleniumDDT/Pages/Logs/" + 'test_ap_' + str(date.today()) + '.log'
        log = Log("__example_test__ ", logger_file)
        self.logger = log.logger

    def test_name_input(self):
        """
        Name: Artiom
        Function Name: test_search
        Description:
        """
        try:
            self.driver.get(os.getenv('URL'))
            self.enter_text(self.locator.input_name, 'adad')
            x = self.driver.find_element(*self.locator.input_name).get_attribute('value')
            self.assertEqual(x, 'adad')  # add assertion here
            self.logger.info(f"{self.test_name_input.__doc__}\nActual: {x} Expected:(x > 0 and not None)\n")
        except Exception as e:
            self.logger.exception(f"{self.test_name_input.__doc__}{e}")
            raise

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
