import datetime


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
        time = str(datetime.datetime.now()).replace(' ', '-').replace('.', '-').replace(':', '_')
        print(time)
        if self.driver.save_screenshot(self.dir_path + '/' + file_name + '_' + time + '.png'):
            print("Screenshot Saved")
        else:
            print("Fail to save screenshot")
