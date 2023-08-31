from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "your email here"
ACCOUNT_PASSWORD = "your pass here"
PHONE = Your phone number here

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3689679460&f_LF=f_AL&geoId=102257491&keywords=python%20"
           "developer&location=London%2C%20England%2C%20United%20Kingdom")

time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for listing in all_listings:
    print("Opening Listing")
    listing.click()

    try:
        time.sleep(5)
        apply_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        time.sleep(2)
        phone = driver.find_element(By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        while True:
            try:
                next_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Continue to next step"]')
                next_button.click()
                time.sleep(2)
            except NoSuchElementException:
                break

        try:
            review_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Review your application"]')
            review_button.click()
            time.sleep(2)
        except NoSuchElementException:
            pass

        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Submit application"]')
        submit_button.click()
    except NoSuchElementException:
        pass

