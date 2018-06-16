from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import locators_c
from urllib.parse import urlparse, urljoin


class page_base_c:
    '''
    a base page class that can: 
        open a page and wait until it is loaded
        throw an exception if a wrong page loaded or loading timed out, used in tests
        help diagnose loading errors 
    '''
    _base_url = None
    _driver = None
    _url = None

    def __init__(self, driver, base_url='https://e.mail.ru/', timeout=15, wait_until_ready=True) -> None:
        self._driver = driver
        self._base_url = base_url
        self._timeout = timeout

        if wait_until_ready:
            self.wait_until_ready()

    def find_element(self, *locator):
        return self._driver.find_element(*locator)

    @property
    def url(self):
        return urljoin(self._base_url, self._url)

    @property
    def driver(self):
        return self._driver

    def wait_until_ready(self):
        '''called from init; awaits page readiness; if timed out, reports reasons'''
        try:
            WebDriverWait(self._driver, self._timeout).until(lambda _: self.ready(),
                                                             "wait failed after %s seconds" % self._timeout)
        except TimeoutException as e:
            self.ready(diag=True)
            raise


    @staticmethod
    def url_paths_equal(url1, url2):
        '''compare url paths, part of the check that we landed at the right page'''
        p1 = urlparse(url1)
        p2 = urlparse(url2)
        return p1[:3] == p2[:3]

    def report(self, msg):
        print(msg)


    
    def ready(self, diag=False):
        '''check if the page is what we expect and ready'''
        if not self.url_paths_equal(self._driver.current_url, self.url):
            if diag:
                self.report("current url <> expected url: %s, %s" % (self._driver.current_url, self.url))
            return False
        loc = getattr(self, 'locator', None)
        if not loc:
            return True
        elt = self.find_element(*loc)
        if not elt:
            if diag:
                self.report("element missing: %s %s " % (loc[0], loc[1]))
            return False
        if not elt.is_displayed():
            if diag:
                self.report("element not visible: %s %s " % (loc[0], loc[1]))
            return False
        return True


class login_page_c(page_base_c):
    ''' login page '''

    _url = '/'

    def __init__(self, driver, base_url='https://mail.ru/', **kwargs) -> None:
        self.locator = locators_c.main_login.AUTH_LINK
        super().__init__(driver, base_url=base_url, **kwargs)

    def enter_username(self, user):
        self.find_element(*locators_c.main_login.USERNAME).send_keys(user['username'])

    def enter_password(self, user):
        self.find_element(*locators_c.main_login.PASSWORD).send_keys(user['password'])

    def click_login(self):
        self.find_element(*locators_c.main_login.SUBMIT).click()

    
    def login(self, user, logout=True):
        ''' login service '''
        if logout:
            logout_link = self.find_element(*locators_c.main_logged_in.LOGOUT)
            if logout_link.is_displayed():
                logout_link.click()

        self.enter_username(user)
        self.enter_password(user)
        self.click_login()

    def login_valid(self, user):
        self.login(user)
        return main_page_logged_in_c(self.driver)

    def login_invalid(self, user):
        self.login(user)
        return main_page_login_error_c(self.driver)


class main_page_logged_in_c(page_base_c):
    ''' main page, logged in '''
    _url = '/messages/inbox/'

    def __init__(self, driver, **kwargs) -> None:
        self.locator = locators_c.main_logged_in.LOGOUT
        super().__init__(driver, **kwargs)
    
    def compose(self):
        ''' compose link '''
        self.find_element(*locators_c.main_logged_in.COMPOSE).click()
        return compose_page_c(self.driver)
    
    def logout(self):
        ''' logout service '''
        logout=self.find_element(*locators_c.main_logged_in.LOGOUT)
        logout.click()
        return login_page_c(self.driver)


class compose_page_c(page_base_c):
    ''' e-mail compose page '''
    _url = '/compose/'

    def __init__(self, driver, **kwargs) -> None:
        super().__init__(driver, **kwargs)

    def enter_recipient(self, recipient):
        rcpt = self.find_element(*locators_c.compose.TO)
        rcpt.send_keys(recipient)

    def enter_subject(self, subject):
        rcpt = self.find_element(*locators_c.compose.SUBJECT)
        rcpt.send_keys(subject)

    def enter_body(self, body):
        edit_iframe = self.find_element(*locators_c.compose.COMPOSE_IFRAME)
        self.driver.switch_to.frame(edit_iframe)
        edit = self.find_element(*locators_c.compose.COMPOSE_EDIT)
        edit.clear()
        edit.send_keys(body)
        self.driver.switch_to_default_content()

    def submit(self):
        self.find_element(*locators_c.compose.SUBMIT).click()

    def send_mail(self, recipient, body, subject=None):
        ''' send email service '''
        self.enter_recipient(recipient)
        self.enter_body(body)
        if subject:
            self.enter_subject(subject)
        self.submit()
        return mail_sent_c(self._driver)


class mail_sent_c(page_base_c):
    ''' sent e-mail page '''
    _url = '/sendmsgok'

    def __init__(self, driver, **kwargs) -> None:
        super().__init__(driver, **kwargs)

    def logout(self):
        self.find_element(*locators_c.main_logged_in.LOGOUT).click()
        return login_page_c(self.driver)


class main_page_login_error_c(page_base_c):
    ''' login page with error message, we arrive here after an invalid logging in '''
    _url = '/'

    def __init__(self, driver, base_url='https://mail.ru/', **kwargs) -> None:
        self.locator = locators_c.main_login_error.LOGIN_ERROR_MSG
        super().__init__(driver, base_url=base_url, **kwargs)

