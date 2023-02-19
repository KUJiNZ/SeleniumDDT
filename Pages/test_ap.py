import os
import re
import unittest
from datetime import date
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Utilities.screenshoter import Screenshoter
from Utilities.logger import Logger
from Utilities.datareader import Datareader

from Pages.base_page import BasePage
from Locators.locators import PageLocators

load_dotenv('.env.test')


class TestAP(unittest.TestCase, BasePage):

    def setUp(self):
        BasePage.__init__(self, webdriver.Chrome())
        self.driver = webdriver.Chrome()
        self.locator = PageLocators()
        # WAIT
        self.wait = WebDriverWait(self.driver, 10)

        # INIT Datareader of JSON
        self.util = Datareader('DATA/DATA.json')
        self.expected = self.util.get_data()

        # INIT LOGGER
        logger_file = 'Logs/' + 'test_ap_' + str(date.today()) + '.log'
        self.log = Logger("test_ap_logger ", logger_file)
        self.logger = self.log.logger
        self.driver.get(os.getenv('URL'))

        # INIT SCREENSHOTER
        self.screenshoter = Screenshoter(self.driver, 'D:/PythonProjects/SeleniumDDT/Pages/Screenshots')

    def tearDown(self):
        self.driver.quit()

    # PERSON INFO AREA
    def test_fname_input(self):
        """
        Name: Artiom
        Function Name: test_name_input
        Description: testing input first name field
        """
        try:
            fname_regex = '^[A-Z]\D\S[a-z]{1,40}'
            for i in range(len(self.expected['fname']) - 1):

                # Positive test
                if re.match(fname_regex, self.expected['fnames'][i]):
                    # Inserting text to check
                    self.enter_text(self.locator.fname, self.expected['fnames'][i])
                    # Finding input element
                    x = self.driver.find_element(*self.locator.fname)
                    # Getting inserted text from input
                    value = x.get_attribute('value')
                    # Asserting if text in element is the same in json
                    self.assertEqual(value, self.expected['fnames'][i])
                    self.logger.info(self.log.message_build(self.test_fname_input.__doc__, x,
                                                            value, self.expected['fnames'][i]))
                    x.clear()

                # Negative test
                else:
                    # Inserting text to check
                    self.enter_text(self.locator.fname, self.expected['fnames'][i])
                    # Finding input element
                    y = self.expected['fnames'][i]
                    x = self.driver.find_element(*self.locator.fname)
                    # Getting inserted text from input
                    value = x.get_attribute('validationMessage')
                    # Asserting valid massage that must be in input field cause text input is not valid
                    # If message isn't popped that means bug
                    self.assertNotEqual(value, '')
                    self.logger.info(self.log.message_build(self.test_fname_input.__doc__, x,
                                                            value, self.expected['fnames'][i]))
                    x.clear()
        except Exception as e:
            self.screenshoter.page_screenshot('test_last_name_input')
            self.logger.exception(f"{self.test_fname_input.__doc__}{e}")
            raise

    def test_last_name_input(self):
        """
        Name: Artiom
        Function Name: test_last_name_input
        Description: testing input last name field
        """
        try:
            fname_regex = '^[A-Z]\D\S[a-z]{1,3}'
            for i in range(len(self.expected['lnames']) - 1):

                # Positive test
                if re.match(fname_regex, self.expected['lnames'][i]):
                    # Inserting text to check
                    self.enter_text(self.locator.lname, self.expected['lnames'][i])
                    # Finding input element
                    x = self.driver.find_element(*self.locator.lname)
                    # Getting inserted text from input
                    value = x.get_attribute('value')
                    # Asserting if text in element is the same in json
                    self.assertEqual(value, self.expected['lnames'][i])
                    self.logger.info(self.log.message_build(self.test_last_name_input.__doc__, x,
                                                            value, self.expected['lnames'][i]))
                    x.clear()

                # Negative test
                else:
                    # Inserting text to check
                    self.enter_text(self.locator.lname, self.expected['lnames'][i])
                    # Finding input element
                    y = self.expected['lnames'][i]
                    x = self.driver.find_element(*self.locator.lname)
                    # Getting inserted text from input
                    value = x.get_attribute('validationMessage')
                    # Asserting valid massage that must be in input field cause text input is not valid
                    # If message isn't popped that means bug
                    self.assertNotEqual(value, '')
                    self.logger.info(self.log.message_build(self.test_last_name_input.__doc__, x,
                                                            value, self.expected['lnames'][i]))
                    x.clear()
        except Exception as e:
            self.screenshoter.page_screenshot('test_last_name_input')
            self.logger.exception(f"{self.test_fname_input.__doc__}{e}")
            raise

    def test_email_input(self):
        """
        Name: Artiom
        Function Name: test_email_input
        Description: testing input email field
        """
        try:
            email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{1,3}$'
            # Passing through all data json emails
            for i in range(len(self.expected['emails']) - 1):

                # Positive test
                if re.match(email_regex, self.expected['emails'][i]):
                    # Inserting text to check
                    self.enter_text(self.locator.fname, self.expected['emails'][i])
                    # Finding input element
                    x = self.driver.find_element(*self.locator.fname)
                    # Getting inserted text from input
                    value = x.get_attribute('value')
                    # Asserting if text in element is the same in json
                    self.assertEqual(value, self.expected['emails'][i])
                    self.logger.info(self.log.message_build(self.test_email_input.__doc__, x,
                                                            value, self.expected['emails'][i]))
                    x.clear()

                # Negative test
                else:
                    self.enter_text(self.locator.fname, self.expected['emails'][i])
                    # Finding input element
                    x = self.driver.find_element(*self.locator.fname)
                    # Getting inserted text from input
                    value = x.get_attribute('validationMessage')
                    # Asserting valid massage that must be in input field cause text input is not valid
                    # If message isn't popped that means bug
                    self.assertNotEqual(value, '')
                    self.logger.info(self.log.message_build(self.test_email_input.__doc__, value,
                                                            value, Exception))
                    x.clear()
        except Exception as e:
            self.screenshoter.page_screenshot('test_email_input')
            self.logger.exception(f"{self.test_email_input.__doc__}{e}")
            raise

    def test_phone_input(self):
        """
        Name: Artiom
        Function Name: test_phone_input
        Description: testing input phone field
        """
        try:
            # Only digits without whitespace and in len of 8 digits exactly
            phone_regex = '\d\S{7}$'
            # Passing through all data json phones
            for i in range(len(self.expected['phones']) - 1):

                # Positive test
                if re.match(phone_regex, self.expected['phones'][i]):
                    # Inserting text to check
                    self.enter_text(self.locator.fname, self.expected['phones'][i])
                    # Finding input element
                    x = self.driver.find_element(*self.locator.fname)
                    # Getting inserted text from input
                    value = x.get_attribute('value')
                    # Asserting if text in element is the same in json
                    self.assertEqual(value, self.expected['phones'][i])
                    self.logger.info(self.log.message_build(self.test_phone_input.__doc__, x,
                                                            value, self.expected['phones'][i]))
                    x.clear()

                # Negative test
                else:
                    self.enter_text(self.locator.fname, self.expected['phones'][i])
                    # Finding input element
                    x = self.driver.find_element(*self.locator.fname)
                    # Getting inserted text from input
                    value = x.get_attribute('validationMessage')
                    # Asserting valid massage that must be in input field cause text input is not valid
                    # If message isn't popped that means bug
                    self.assertNotEqual(value, '')
                    self.logger.info(self.log.message_build(self.test_email_input.__doc__, value,
                                                            value, Exception))
                    x.clear()
        except Exception as e:
            self.screenshoter.page_screenshot('test_phone_input')
            self.logger.exception(f"{self.test_phone_input.__doc__}{e}")
            raise

    def test_city_combobox(self):
        """
        Name: Artiom
        Function Name: test_city_combobox
        Description: testing city combobox list,looking for combobox and asserting his option text with json data
        """
        try:
            # Finding node of select combobox
            x = self.driver.find_element(*self.locator.city)
            select = Select(x)
            # Getting data from json that must be in combobox k is index v is text in option
            for k, v in self.expected["city"].items():
                # Getting option by index
                select.select_by_index(int(k))
                # Getting text of selected option
                y = select.first_selected_option.text
                # Assert text of selected option and text in json
                self.assertEqual(y, v)
                self.logger.info(self.log.message_build(self.test_fname_input.__doc__, x, y, v))
        except Exception as e:
            self.screenshoter.page_screenshot('test_city_combobox')
            self.logger.exception(f"{self.test_fname_input.__doc__}{e}")
            raise

    def test_mobile_combobox(self):
        """
        Name: Artiom
        Function Name: test_mobile_combobox
        Description: testing city combobox list,looking for combobox and asserting his option text with json data
        """
        try:
            # Finding node of select combobox
            x = self.driver.find_element(*self.locator.mobile)
            select = Select(x)
            # Getting data from json that must be in combobox k is index v is text in option
            for k, v in self.expected["mobile"].items():
                # Getting option by index
                select.select_by_index(int(k))
                # Getting text of selected option
                y = select.first_selected_option.text
                # Assert text of selected option and text in json
                self.assertEqual(y, v)
                self.logger.info(self.log.message_build(self.test_fname_input.__doc__, x, y, v))
        except Exception as e:
            self.screenshoter.page_screenshot('test_mobile_combobox')
            self.logger.exception(f"{self.test_fname_input.__doc__}{e}")
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
                    self.log.message_build(self.test_radios.__doc__, radios[i], radios[i].is_selected(), True))
        except Exception as e:
            self.screenshoter.page_screenshot('test_radios')
            self.logger.exception(f"{self.test_radios.__doc__}{e}")
            raise

    def test_course_checkboxes1(self):
        """
        Name: Artiom
        Function Name: test_course_checkboxes1
        Description: testing course checkboxes is working
        """
        try:
            checkboxes = self.driver.find_elements(*self.locator.checkboxes_course1)
            for i in range(len(checkboxes)):
                checkboxes[i].click()
                self.assertTrue(checkboxes[i].is_selected())
                self.logger.info(self.log.message_build(self.test_course_checkboxes1.__doc__, checkboxes[i],
                                                        checkboxes[i].is_selected(), True))
        except Exception as e:
            self.screenshoter.page_screenshot('test_course_checkboxes1')
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
                self.logger.info(self.log.message_build(self.test_gender_checkboxes.__doc__, checkboxes[i],
                                                        checkboxes[i].is_selected(), True))
        except Exception as e:
            self.screenshoter.page_screenshot('test_gender_checkboxes')
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
                self.logger.info(self.log.message_build(self.test_course_checkboxes2.__doc__, checkboxes[i],
                                                        checkboxes[i].is_selected(), True))
        except Exception as e:
            self.screenshoter.page_screenshot('test_course_checkboxes2')
            self.logger.exception(f"{self.test_course_checkboxes2.__doc__}{e}")
            raise

    def test_clear(self):
        """
        Name: Artiom
        Function Name: test_clear
        Description: testing clearing input fields and radios and checkboxes cleared after clicking on Clear button
        """
        try:

            radios_and_checkboxes = []
            input_fields = []
            # Searching and filling inputs field from json data
            for input_field in self.locator.person_input_fields:
                input_fields.append(self.driver.find_element(*input_field))
                self.enter_text(input_field, self.expected[input_field[1]])

            # Searching radios and checkboxes and selecting them
            for checkbox in self.locator.checkboxes_and_radios:
                radios_and_checkboxes.append(self.driver.find_elements(*checkbox))
            for ls in radios_and_checkboxes:
                for item in ls:
                    item.click()

            # Clicking on button Clear
            self.driver.find_element(*self.locator.clear_button).click()

            # Checking if inputs cleared
            for input_field in input_fields:
                self.assertEqual(input_field.get_attribute('value'), '')
                self.logger.info(self.log.message_build(self.test_clear.__doc__, input_field,
                                                        input_field.get_attribute('value'), ''))

            # Checking if radios and checkboxes is unselected
            for ls in radios_and_checkboxes:
                for item in ls:
                    self.assertFalse(item.is_selected())
                    self.logger.info(self.log.message_build(self.test_clear.__doc__, item,
                                                            item.get_attribute('name'), False))
        except Exception as e:
            self.screenshoter.page_screenshot('test_clear')
            self.logger.exception(f"{self.test_course_checkboxes2.__doc__}{e}")
            raise

    def test_send(self):
        """
        Name: Artiom
        Function Name: test_send
        Description: testing button Send that connected to input fields in person info area
        """
        try:
            # Searching all inputs must be field that connected to Send button
            for input_field in self.locator.person_input_fields:
                x = self.driver.find_element(*input_field)
                # Input is empty that means pushing Send button must be validation message on the input
                self.driver.find_element(*self.locator.send_button).click()
                # Getting validation message,if he wasn't popped by default he is ''
                valid_msg = x.get_attribute("validationMessage")
                # If validation message is empty he wasn't popped that is fail cause input must be filled
                self.assertTrue(valid_msg != '')
                # Filling the field to check next field
                self.enter_text(input_field, self.expected[input_field[1]])
                self.logger.info(self.log.message_build(self.test_send.__doc__, x,
                                                        x.get_attribute('value'), 'Validation message'))
        except Exception as e:
            self.screenshoter.page_screenshot('test_clear')
            self.logger.exception(f"{self.test_send.__doc__}{e}")
            raise

    # JS Buttons area
    def test_set_text(self):
        """
        Name: Artiom
        Function Name: test_set_text
        Description: testing js button Set Text,button calling to
        prompt alert where need to set text and check the text in fieldset
        """
        try:
            # Finding button Set Text
            self.driver.find_element(*self.locator.JSB_settext).click()
            # Switching to prompt alert
            alert = self.driver.switch_to.alert
            # Inserting text to prompt alert
            alert.send_keys(self.expected['jsb_fieldset'])
            # Submit prompt alert
            alert.accept()
            # Finding fieldset where text inserted from prompt alert
            x = self.driver.find_element(*self.locator.JSB_fieldset)
            # Asserting text in fieldset and data json
            self.assertEqual(x.text, self.expected['jsb_fieldset'])
            self.logger.info(self.log.message_build(self.test_send.__doc__, x,
                                                    x.text, self.expected['jsb_fieldset']))
        except Exception as e:
            self.screenshoter.page_screenshot('test_clear')
            self.logger.exception(f"{self.test_set_text.__doc__}{e}")
            raise

    def test_start_loading(self):
        """
        Name: Artiom
        Function Name: test_start_loading
        Description: testing js button Start loadin,button have to switch text
        """
        try:
            # Finding text
            x = self.driver.find_element(*self.locator.JS_text)
            self.assertTrue(x.text, self.expected['jsb_text'][0])
            self.logger.info(self.log.message_build(self.test_start_loading.__doc__, x,
                                                    x.text, self.expected['jsb_text'][0]))
            # Finding button Start Loading and click on him
            self.driver.find_element(*self.locator.JSB_startloading).click()
            # Asserting if text is switched
            self.assertTrue(
                self.wait.until(ec.text_to_be_present_in_element(self.locator.JS_text, self.expected['jsb_text'][1])))
            self.logger.info(self.log.message_build(self.test_start_loading.__doc__, x,
                                                    x.text, self.expected['jsb_text'][1]))
        except Exception as e:
            self.screenshoter.page_screenshot('test_start_loading')
            self.logger.exception(f"{self.test_set_text.__doc__}{e}")
            raise


if __name__ == '__main__':
    unittest.main()
