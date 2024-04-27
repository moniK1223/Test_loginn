# import time
# import pytest
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# @pytest.fixture(scope='class')
# def _drivers():
#     driver = webdriver.Chrome(options=opts)
#     driver.get('https://demowebshop.tricentis.com/')
#     time.sleep(2)
#     yield driver
#     driver.close()
#
# ## _drivers --> driver = webdriver.Chrome(options=opts)
#
# class TestDemoLogin:
#
#     def test_click_login(self, _drivers):
#         _drivers.find_element('xpath', '//a[text()="Log in"]').click()
#         time.sleep(1)
#
#     def test_login_email(self, _drivers):
#         _drivers.find_element('xpath', '//input[@id="Email"]').send_keys('meghashankar@gmail.com')
#
#     def test_login_pwd(self, _drivers):
#         _drivers.find_element('xpath', '//input[@id="Password"]').send_keys('megha@12345')
#
#----------------------------------

## using conftest

import time

class TestDemoLogin:

    def test_click_login(self, _drivers):
        _drivers.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(1)

    def test_login_email(self, _drivers):
        _drivers.find_element('xpath', '//input[@id="Email"]').send_keys('meghashankar@gmail.com')

    def test_login_pwd(self, _drivers):
        _drivers.find_element('xpath', '//input[@id="Password"]').send_keys('megha@12345')



















