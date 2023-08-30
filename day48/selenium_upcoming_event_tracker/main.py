from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

upcoming_event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
upcoming_event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}
for n in range(len(upcoming_event_times)):
    events[n] = {
        "time": upcoming_event_times[n].text,
        "name": upcoming_event_names[n].text,
    }
print(events)

driver.quit()
