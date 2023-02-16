from selenium.webdriver.common.by import By


class PageLocators(object):
    fname = (By.NAME, 'fname')
    lname = (By.NAME, 'lname')
    email = (By.NAME, 'email')
    city = (By.NAME,'City')
    mobile = (By.NAME, 'areaCode')
    phone = (By.ID,'phone')
    radios_gender = (By.XPATH, "//input[@type = 'radio' and @name ='gender']")
    checkboxes_course1 = (By.XPATH, "//input[@type = 'checkbox' and (@name ='math' or @name ='pyhs')]")
    checkboxes_gender = (By.XPATH, "//input[@type = 'checkbox' and @name ='gender']")
    checkboxes_course2 = (By.XPATH, "//input[@type = 'checkbox' and (@name ='bio' or @name ='chem' or @name ='eng')]")

