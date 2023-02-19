import unittest
from unittest import main

from selenium import webdriver

from Pages import test_ap, test_nextpage
from Pages.test_ap import TestAP
from Pages.base_page import BasePage
from Pages.test_nextpage import TestNextPage

if __name__ == "__main__":
    # driver = webdriver.Chrome()
    # ts1 = TestAP(driver)
    # ts1.run()
    test_ap_suite = unittest.defaultTestLoader.loadTestsFromModule(test_ap)
    unittest.TextTestRunner().run(test_ap_suite)

    test_nextpage_suite = unittest.defaultTestLoader.loadTestsFromModule(test_nextpage)
    unittest.TextTestRunner().run(test_nextpage_suite)
