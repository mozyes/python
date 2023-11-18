from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL_ID = "Your id here"
PASSWORD = "Your password here"
MAIL_TO_ID = "Boss id here"
SUBJECT = "Your subject here"
MESSAGE = """
Your Mail here!
"""

class EmailSender:
    def __init__(self, email_id, password, mail_to, subject, message):
        self.email_id = email_id
        self.password = password
        self.mail_to = mail_to
        self.subject = subject
        self.message = message
        self.driver = None

    def login(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://login.yahoo.com/")

        time.sleep(5)
        email_field = self.driver.find_element(By.XPATH, "//input[@id='login-username']")
        email_field.send_keys(self.email_id)
        email_field.send_keys(Keys.ENTER)

        time.sleep(30) # this was done to help myself work around 'Are you robot?' thingy.
        password_field = self.driver.find_element(By.XPATH, "//input[@id='login-passwd']")
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.ENTER)

        time.sleep(5)

    def write_mail_to(self):
        time.sleep(5)
        self.driver.get("https://mail.yahoo.com/d/folders/1")

        time.sleep(5)
        compose_mail = self.driver.find_element(By.XPATH, "//a[@aria-label='Compose']")
        compose_mail.click()

        time.sleep(5)
        mail_to = self.driver.find_element(By.XPATH, "//input[@id='message-to-field']")
        mail_to.send_keys(self.mail_to)

        time.sleep(5)
        subject = self.driver.find_element(By.XPATH, "//input[@placeholder='Subject']")
        subject.send_keys(self.subject)

        time.sleep(5)
        message = self.driver.find_element(By.XPATH, "//div[@aria-label='Message body']")
        message.send_keys(self.message)

        time.sleep(5)
        send_mail = self.driver.find_element(By.XPATH, "//button[@title='Send this email']")
        send_mail.click()

to_boss = EmailSender(EMAIL_ID, PASSWORD, MAIL_TO_ID, SUBJECT, MESSAGE)
to_boss.login()
to_boss.write_mail_to()
