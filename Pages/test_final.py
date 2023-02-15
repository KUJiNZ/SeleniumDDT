from selenium import webdriver
from Pages.base_page import BasePage
if __name__ == "__main__":
    driver = webdriver.Chrome()
    b = BasePage(driver)


