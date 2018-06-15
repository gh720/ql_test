import unittest
from unittest import TestCase

import os

import sys
from selenium import webdriver

from pages.fixtures import fixtures_c
from pages.main import login_page_c


class base_c(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://mail.ru/")


    def tearDown(self):
        self.driver.close()
        super().tearDown()


class mail_ru_login_test(base_c):

    def test_sign_in_with_valid_user(self):
        login_page = login_page_c(self.driver)
        logged_in_page = login_page.login_valid(fixtures_c.users.valid_creds)
        logged_in_page.logout()

    def test_sign_in_with_invalid_user(self):
        login_page = login_page_c(self.driver)
        login_page.login_invalid(fixtures_c.users.invalid_creds)

class mail_ru_send_email_test(base_c):

    def test_send_email(self):
        login_page = login_page_c(self.driver)
        sent_page= login_page \
            .login_valid(fixtures_c.users.valid_creds)\
            .compose() \
            .send_mail(fixtures_c.mail.recipient, fixtures_c.mail.body)
        sent_page.logout()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromName('mail_ru_test')
    unittest.TextTestRunner(verbosity=2).run(suite)
