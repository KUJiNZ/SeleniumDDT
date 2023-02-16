from selenium.webdriver.common.by import By


class PageLocators(object):
    fname = (By.NAME, 'fname')
    lname = (By.NAME, 'lname')
    email = (By.NAME, 'email')
    city = (By.NAME,'City')
    mobile = (By.NAME, 'areaCode')

