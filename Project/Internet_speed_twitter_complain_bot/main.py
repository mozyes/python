from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 250
PROMISED_UP = 125
TWITTER_EMAIL = YOUR ID HERE
TWITTER_PASSWORD = YOUR PASSWORD HERE
USERNAME = YOUR USERNAME HERE


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        pass
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        go_button = self.driver.find_element(By.CLASS_NAME, "start-button")
        go_button.click()

        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(self.up)
        print(self.down)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")

        time.sleep(2)
        log_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div'
                                                    '/div/div[3]/div[5]/a')
        log_in.click()
        time.sleep(5)

        t_email = self.driver.find_element(By.NAME, "text")
        t_email.send_keys(TWITTER_EMAIL)
        t_email.send_keys(Keys.ENTER)

        time.sleep(5)
        user_name = self.driver.find_element(By.NAME, "text")
        user_name.send_keys(USERNAME)
        user_name.send_keys(Keys.ENTER)

        time.sleep(5)
        t_password = self.driver.find_element(By.NAME, "password")
        t_password.send_keys(TWITTER_PASSWORD)
        t_password.send_keys(Keys.ENTER)

        time.sleep(5)

        tweet_compose = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
        tweet = (f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for "
                 f"{PROMISED_DOWN}down/{PROMISED_UP}up?")
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div'
                                                          '/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]'
                                                          '/div[2]/div/div/div[2]/div[3]')
        tweet_button.click()
        time.sleep(2)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
