from datetime import date
from selenium import webdriver


class Screenshoter(object):

    def __init__(self, driver, dir_path):
        """
        Description:Constructor must get reference of webdriver and directory to save screenshots
        :param driver: webdriver of selenium
        :param dir_path: path to save screenshots
        """
        self.driver = driver
        self.dir_path = dir_path

    def page_screenshot(self, file_name):
        # print(self.dir_path + '/' + file_name + str(datetime.now()) + '.png')
        if self.driver.save_screenshot(self.dir_path + '/' + file_name + '_' + str(date.today()) + '.png'):
            print("Screenshot Saved")
        else:
            print("Fail to save screenshot")
