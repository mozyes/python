from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

EMAIL_ID = "Your email"
PASSWORD = "Your pass"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

time.sleep(2)
log_in = driver.find_element(By.LINK_TEXT, value="Log in")
log_in.click()

time.sleep(3)
log_in_fb = driver.find_element(By.CSS_SELECTOR, value='button[aria-label="Log in with Facebook"]')
log_in_fb.click()

time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email_field = driver.find_element(By.XPATH, '//*[@id="email"]')
email_field.send_keys(EMAIL_ID)

password_field = driver.find_element(By.XPATH, '//*[@id="pass"]')
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

allow_button = driver.find_element(By.XPATH, value='//*[@id="t-1801918317"]/main/div[1]/div/div/div[3]/button[1]'
                                                   '/div[2]')
allow_button.click()

not_interested_button = driver.find_element(By.XPATH, value='//*[@id="t-1801918317"]/main/div[1]/div/div/div[3]/button'
                                                            '[2]')
not_interested_button.click()

for n in range(100):


    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH,
            '//*[@id="t-73537241"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
            time.sleep(2)

driver.quit()
