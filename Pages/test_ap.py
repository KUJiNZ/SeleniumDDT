import os
import unittest
from datetime import date
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.support.select import Select

from UTILITIES.log import Log
from UTILITIES.utilities import Utilities
from Pages.base_page import BasePage
from Locators.locators import PageLocators

load_dotenv('.env.test')


class TestAP(unittest.TestCase, BasePage):

    def setUp(self):
        # BasePage.__init__(self, webdriver.Chrome())
        self.driver = webdriver.Chrome()
        self.locator = PageLocators()
        # INIT JSON
        self.util = Utilities('D:/PythonRepos/SeleniumDDTPython/Pages/DATA/DATA.json')
        self.expected = self.util.get_data()
        # INIT LOGGER
        logger_file = "D:/PythonRepos/SeleniumDDTPython/Pages/Logs/" + 'test_ap_' + str(date.today()) + '.log'
        log = Log("__example_test__ ", logger_file)
        self.logger = log.logger
        self.driver.get(os.getenv('URL'))

    def test_name_input(self):
        """
        Name: Artiom
        Function Name: test_name_input
        Description: testing input first name field
        """
        try:
            self.enter_text(self.locator.fname, self.expected['fname'])
            x = self.driver.find_element(*self.locator.fname).get_attribute('value')
            self.assertEqual(x, self.expected['fname'])  # add assertion here
            self.logger.info(f"{self.test_name_input.__doc__}\nActual: {x}, Expected: {self.expected['fname']}\n")
        except Exception as e:
            self.logger.exception(f"{self.test_name_input.__doc__}{e}")
            raise

    def test_last_name_input(self):
        """
        Name: Artiom
        Function Name: test_last_name_input
        Description: testing input last name field
        """
        try:
            self.enter_text(self.locator.fname, self.expected['email'])
            x = self.driver.find_element(*self.locator.fname).get_attribute('value')
            self.assertEqual(x, self.expected['email'])  # add assertion here
            self.logger.info(f"{self.test_name_input.__doc__}\nActual: {x}, Expected: {self.expected['email']}\n")
        except Exception as e:
            self.logger.exception(f"{self.test_name_input.__doc__}{e}")
            raise

    def test_email_input(self):
        """
        Name: Artiom
        Function Name: test_email_input
        Description: testing input email field
        """
        try:
            self.enter_text(self.locator.fname, self.expected['email'])
            x = self.driver.find_element(*self.locator.fname).get_attribute('value')
            self.assertEqual(x, self.expected['email'])  # add assertion here
            self.logger.info(f"{self.test_name_input.__doc__}\nActual: {x}, Expected: {self.expected['email']}\n")
        except Exception as e:
            # self.driver.save_screenshot("D:\\PythonScreenShots\\test.jpg")
            self.logger.exception(f"{self.test_name_input.__doc__}{e}")
            raise

    def test_city_combobox(self):
        """
        Name: Artiom
        Function Name: test_city_combobox
        Description: testing city combobox list,looking for combobox and asserting his option text with json data
        """
        try:
            # Finding node of select combobox
            x = Select(self.driver.find_element(*self.locator.city))
            # Getting data from json that must be in combobox k is index v is text in option
            for k, v in self.expected["city"].items():
                # Getting option by index
                x.select_by_index(int(k))
                # Getting text of selected option
                y = x.first_selected_option.text
                # Assert text of selected option and text in json
                self.assertEqual(y, v)
                self.logger.info(f"{self.test_name_input.__doc__}\nActual: {y}, Expected: {v}\n")
        except Exception as e:
            # self.driver.save_screenshot("D:/PythonRepos/SeleniumDDTPython/Pages/Screenshotstest/test.png")
            self.logger.exception(f"{self.test_name_input.__doc__}{e}")
            raise

    def test_mobile_combobox(self):
        """
        Name: Artiom
        Function Name: test_mobile_combobox
        Description: testing city combobox list,looking for combobox and asserting his option text with json data
        """
        try:
            # Finding node of select combobox
            x = Select(self.driver.find_element(*self.locator.mobile))
            # Getting data from json that must be in combobox k is index v is text in option
            for k, v in self.expected["mobile"].items():
                # Getting option by index
                x.select_by_index(int(k))
                # Getting text of selected option
                y = x.first_selected_option.text
                # Assert text of selected option and text in json
                self.assertEqual(y, v)
                self.logger.info(f"{self.test_name_input.__doc__}\nActual: {y}, Expected: {v}\n")
        except Exception as e:
            # self.driver.save_screenshot("D:\\PythonScreenShots\\test.jpg")
            self.logger.exception(f"{self.test_name_input.__doc__}{e}")
            raise

    def test_phone_input(self):
        """
        Name: Artiom
        Function Name: test_phone_input
        Description: testing input phone field
        """
        try:
            self.enter_text(self.locator.phone, self.expected['phone'])
            x = self.driver.find_element(*self.locator.phone).get_attribute('value')
            self.assertEqual(x, self.expected['phone'])
            self.logger.info(f"{self.test_name_input.__doc__}\nActual: {x}, Expected: {self.expected['phone']}\n")
        except Exception as e:
            # self.driver.save_screenshot("D:\\PythonScreenShots\\test.jpg")
            self.logger.exception(f"{self.test_name_input.__doc__}{e}")
            raise

    def test_radios(self):
        """
        Name: Artiom
        Function Name: test_radios
        Description: testing radios gender is working
        """
        try:
            radios = self.driver.find_elements(*self.locator.radios_gender)
            for i in range(len(radios)):
                radios[i].click()
                self.assertTrue(radios[i].is_selected())
                self.logger.info(
                    f"{self.test_radios.__doc__}\nActual: {radios[i].is_selected()}, Expected: {True}\n")
        except Exception as e:
            # self.driver.save_screenshot("D:\\PythonScreenShots\\test.jpg")
            self.logger.exception(f"{self.test_radios.__doc__}{e}")
            raise

    def test_course_checkboxes1(self):
        """
        Name: Artiom
        Function Name: test_course_checkboxes
        Description: testing course checkboxes is working
        """
        try:
            checkboxes = self.driver.find_elements(*self.locator.checkboxes_course1)
            for i in range(len(checkboxes)):
                checkboxes[i].click()
                self.assertTrue(checkboxes[i].is_selected())
                self.logger.info(
                    f"{self.test_course_checkboxes1.__doc__}\nActual: {checkboxes[i].is_selected()}, Expected: {True}\n")
        except Exception as e:
            # self.driver.save_screenshot("D:\\PythonScreenShots\\test.jpg")
            self.logger.exception(f"{self.test_course_checkboxes1.__doc__}{e}")
            raise

    def test_gender_checkboxes(self):
        """
        Name: Artiom
        Function Name: test_gender_checkboxes
        Description: testing radios gender is working
        """
        try:
            checkboxes = self.driver.find_elements(*self.locator.checkboxes_gender)
            for i in range(len(checkboxes)):
                checkboxes[i].click()
                self.assertTrue(checkboxes[i].is_selected())
                self.logger.info(
                    f"{self.test_gender_checkboxes.__doc__}\nActual: {checkboxes[i].is_selected()}, Expected: {True}\n")
                x = input("Continue?:")
        except Exception as e:
            # self.driver.save_screenshot("D:\\PythonScreenShots\\test.jpg")
            self.logger.exception(f"{self.test_gender_checkboxes.__doc__}{e}")
            raise

    def test_course_checkboxes2(self):
        """
        Name: Artiom
        Function Name: test_course_checkboxes2
        Description: testing course checkboxes is working
        """
        try:
            checkboxes = self.driver.find_elements(*self.locator.checkboxes_course2)
            for i in range(len(checkboxes)):
                checkboxes[i].click()
                self.assertTrue(checkboxes[i].is_selected())
                self.logger.info(
                    f"{self.test_course_checkboxes2.__doc__}\nActual: {checkboxes[i].is_selected()}, Expected: {True}\n")
        except Exception as e:
            # self.driver.save_screenshot("D:\\PythonScreenShots\\test.jpg")
            self.logger.exception(f"{self.test_course_checkboxes2.__doc__}{e}")
            raise

    def test_clear(self):
        """
        Name: Artiom
        Function Name: test_course_checkboxes2
        Description: testing course checkboxes is working
        """
        try:
            input_fields = []
            for e in self.locator.person_input_fields:
                input_fields.append(self.driver.find_element(*e))
            for e in input_fields:
                x = e.get_attribute('value')
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                # self.assertTrue(checkboxes[i].is_selected())
                # self.logger.info(
                #     f"{self.test_course_checkboxes2.__doc__}\nActual: {checkboxes[i].is_selected()}, Expected: {True}\n")
        except Exception as e:
            # self.driver.save_screenshot("D:\\PythonScreenShots\\test.jpg")
            self.logger.exception(f"{self.test_course_checkboxes2.__doc__}{e}")
            raise

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
