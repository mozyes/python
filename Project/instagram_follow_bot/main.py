from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time

EMAIL_ID = "Your Id Here"
PASSWORD = "Your Pass here"
SIMILAR_ACCOUNT = "ACCOUNT ID HERE"

class InstaFollower:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.driver = None

    def login(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.instagram.com/")

        time.sleep(5)
        email_field = self.driver.find_element(By.XPATH, "//input[@name='username']")
        email_field.send_keys(self.email)

        password_field = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys(self.password)

        time.sleep(5)

        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()

        time.sleep(5)
        not_now_button = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]"
                                                            "/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/"
                                                            "div[1]/div[1]/div[1]/div[1]/div[1]")
        not_now_button.click()

        time.sleep(5)
        notification_button = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/"
                                                                 "div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/"
                                                                 "div[3]/button[2]")
        notification_button.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")

        time.sleep(5)
        followers = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/"
                                                       "div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/"
                                                       "header[1]/section[1]/ul[1]/li[2]/a[1]")
        followers.click()

        time.sleep(3)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.XPATH, "//button[@class='_acan _acap _acas _aj1-']")
        print(all_buttons)
        for button in all_buttons:
            try:
                time.sleep(2)
                button.click()
            except ElementClickInterceptedException:
                time.sleep(2)
                following_button = self.driver.find_element(By.XPATH, "//button[@class='_acan _acap _acat _aj1-']")
                following_button.click()
                time.sleep(2)
                cancel_button = self.driver.find_element(By.XPATH, "//button[@class='_a9-- _a9_1']")
                cancel_button.click()

insta_follower = InstaFollower(EMAIL_ID, PASSWORD)
insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()

