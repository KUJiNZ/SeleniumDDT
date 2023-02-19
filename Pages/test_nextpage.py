import os
import re
import unittest
from datetime import date
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Utilities.screenshoter import Screenshoter
from Utilities.logger import Logger
from Utilities.datareader import Datareader

from Pages.base_page import BasePage
from Locators.locators import PageLocators

load_dotenv('.env.test')


class TestNextPage(unittest.TestCase, BasePage):
    def setUp(self):
        BasePage.__init__(self, webdriver.Chrome())
        # self.driver = webdriver.Chrome()
        self.locator = PageLocators()

        # EXPLICIT WAIT
        self.wait = WebDriverWait(self.driver, 10)

        # INIT Datareader of JSON
        self.util = Datareader('DATA/DATA.json')
        self.expected = self.util.get_data()

        # INIT LOGGER
        logger_file = 'Logs/' + 'test_nextpage_' + str(date.today()) + '.log'
        self.log = Logger("test_nextpage_logger ", logger_file)
        self.logger = self.log.logger
        self.driver.get(os.getenv('URL'))

        # INIT SCREENSHOTER
        self.screenshoter = Screenshoter(self.driver, 'D:/PythonProjects/SeleniumDDT/Pages/Screenshots')

        # WINDOW HANDLES
        self.parent_handle = self.driver.current_window_handle

    def tearDown(self):
        self.driver.quit()

    def test_link_next_page(self):
        """
        Name: Artiom
        Function Name: test_link_next_page
        Description: testing NextPage link in Automation Project html by getting page title
        """
        try:
            # Find and open link in new tab
            x = self.driver.find_element(*self.locator.next_page)
            self.driver.execute_script('window.open(arguments[0]);', x)
            # Switch to new opened tab
            self.driver.switch_to.window(self.driver.window_handles[1])

            # Wait until page loaded
            self.wait.until(ec.title_is(self.expected['next_page_titles'][0]))

            # Assert if page loaded by title
            self.assertEqual(self.driver.title, self.expected['next_page_titles'][0])
            self.logger.info(self.log.message_build(self.test_link_next_page.__doc__, 'Link NextPage',
                                                    self.driver.title, self.expected['next_page_titles'][0]))

            # Find button that change title and click
            y = self.driver.find_element(*self.locator.np_button_change_title)
            y.click()

            # Assert if button changed the title
            self.assertEqual(self.driver.title, self.expected['next_page_titles'][1])
            self.logger.info(self.log.message_build(self.test_link_next_page.__doc__, y,
                                                    self.driver.title, self.expected['next_page_titles'][1]))
        except Exception as e:
            self.screenshoter.page_screenshot('test_link_next_page')
            self.logger.exception(f"{self.test_link_next_page.__doc__}{e}")
            raise

    def test_links_is_working(self):
        """
        Name: Artiom
        Function Name: test_links_is_working
        Description: testing links opens in Automation Project html by getting page title
        """
        try:
            self.driver.implicitly_wait(10)
            for locator in self.locator.links_set:
                # Find and open link in new tab
                x = self.driver.find_element(*locator)
                y = x.text
                self.driver.execute_script('window.open(arguments[0]);', x)
                # Switch to new opened tab
                self.driver.switch_to.window(self.driver.window_handles[1])
                # Assert if page loaded by title
                self.assertFalse('404' in self.driver.title)
                self.logger.info(
                    self.log.message_build(self.test_link_next_page.__doc__, y, self.driver.title, 'Not 404'))
                # Close current tab
                self.driver.close()
                # Return to calling tab
                self.driver.switch_to.window(self.parent_handle)

        except Exception as e:
            self.screenshoter.page_screenshot('test_links_is_working')
            self.logger.exception(f"{self.test_link_next_page.__doc__}{e}")
            raise


if __name__ == '__main__':
    unittest.main()
