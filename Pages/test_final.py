import unittest
from selenium import webdriver

from Pages import test_ap
from Pages import test_nextpage
from Pages.test_ap import TestAP

if __name__ == "__main__":
    # driver = webdriver.Chrome()
    # test_ap = TestAP(driver)
    # test_ap.setUp()
    # # test_ap.test_fname_input()
    # test_ap.run()
    # print(test_ap.countTestCases())
    # # unittest.main(defaultTest='test_case')
    unittest.main('test_ap')
    unittest.main('test_nextpage')
