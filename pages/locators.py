from selenium.webdriver.common.by import By

class locators_c:
    class main_login:
        USERNAME = (By.CSS_SELECTOR, "input#mailbox\\:login")
        PASSWORD = (By.CSS_SELECTOR, "input#mailbox\\:password")
        SUBMIT = (By.CSS_SELECTOR, "label#mailbox\\:submit > input[type=submit]")
        AUTH_LINK = (By.CSS_SELECTOR, "a#PH_authLink")

    class main_logged_in:
        LOGOUT = (By.CSS_SELECTOR, "a#PH_logoutLink")
        COMPOSE = (By.CSS_SELECTOR, "a.b-toolbar__btn[data-name='compose']")
        # COMPOSE = (By.CSS_SELECTOR, "a#mailbox\\:write_letter")

    class main_login_error:
        LOGIN_ERROR_MSG = (By.CSS_SELECTOR, "form#auth div#mailbox\\:error")

    class compose:
        TO = (By.CSS_SELECTOR, "textarea[data-original-name=To]")
        SUBJECT = (By.CSS_SELECTOR, "div[data-label=Subject] input[name=Subject]")
        COMPOSE_IFRAME = (By.CSS_SELECTOR, "div.compose__editor td.mceIframeContainer > iframe")
        COMPOSE_EDIT = (By.CSS_SELECTOR, "body")
        SUBMIT = (By.CSS_SELECTOR, "div.b-toolbar div[data-name=send]")

    class mail_sent:
        LOGOUT = (By.CSS_SELECTOR, "a#PH_logoutLink")
