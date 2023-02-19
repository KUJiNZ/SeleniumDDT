from selenium.webdriver.common.by import By


class PageLocators(object):
    # Personal Information area
    fname = (By.NAME, 'fname')
    lname = (By.NAME, 'lname')
    email = (By.NAME, 'email')
    city = (By.NAME, 'City')
    mobile = (By.NAME, 'areaCode')
    phone = (By.ID, 'phone')
    radios_gender = (By.XPATH, "//input[@type = 'radio' and @name ='gender']")
    checkboxes_course1 = (By.XPATH, "//input[@type = 'checkbox' and (@name ='math' or @name ='pyhs')]")
    checkboxes_gender = (By.XPATH, "//input[@type = 'checkbox' and @name ='gender']")
    checkboxes_course2 = (By.XPATH, "//input[@type = 'checkbox' and (@name ='bio' or @name ='chem' or @name ='eng')]")
    clear_button = (By.ID, 'CB')
    person_input_fields = [tuple(fname), tuple(lname), tuple(email), tuple(phone)]
    checkboxes_and_radios = [radios_gender, checkboxes_course1, checkboxes_gender, checkboxes_course2]
    send_button = (By.ID, 'send')

    # JS Buttons area
    JSB_fieldset = (By.ID, 'pbyuser')
    JSB_settext = (By.CSS_SELECTOR, 'body > fieldset:nth-child(4) > button:nth-child(5)')
    JS_text = (By.ID, 'startLoad')
    JSB_startloading = (By.CSS_SELECTOR, 'body > fieldset:nth-child(4) > button:nth-child(9)')

    # Links area
    next_page = (By.NAME, 'nextPage')
    windy = (By.NAME, 'myLink')
    tera_santa = (By.NAME, 'myLinkTS')
    java_book = (By.CSS_SELECTOR, 'body > fieldset:nth-child(5) > a:nth-child(8)')
    youtube = (By.CSS_SELECTOR, 'body > fieldset:nth-child(5) > br:nth-child(11)')
    links_set = [windy, tera_santa, java_book, youtube]

    # Next Page area
    np_button_change_title = (By.CSS_SELECTOR, 'body > button')
