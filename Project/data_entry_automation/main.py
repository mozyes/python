from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

research_website_endpoint = ('https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north'
                             '%22%3A37.84418282105567%2C%22east%22%3A-122.22977682758297%2C%22south%22%3A37.6253399158'
                             '2153%2C%22west%22%3A-122.63146444965328%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%'
                             '22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22'
                             'fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7'
                             'B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value'
                             '%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3A'
                             'false%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22'
                             'mapZoom%22%3A12%7D')

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                  "116.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.8"
}

FORM_URL = ('https://docs.google.com/forms/d/e/1FAIpQLSe9FKYo0ldsFZIcpipNOBPqNNfKn5uy8DpnBelJY3w_40xKSQ/'
            'viewform?usp=sf_link')

response = requests.get(research_website_endpoint, headers=header)
content = response.text

soup = BeautifulSoup(content, 'html.parser')

all_link_elements = soup.find_all('a', class_='property-card-link')
all_links = []

for link in all_link_elements:
    href = link["href"]
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

all_address_elements = soup.select(".property-card-link address")
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

all_price_elements = soup.select(".PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1")
all_price = []
for price in all_price_elements:
    all_price.append(price.text.split('+')[0])

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(all_links)):
    driver.get(FORM_URL)

    time.sleep(2)
    address_field = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/"
                                                 "div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")
    price_field = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/"
                                                "div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")
    link_field = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/"
                                              "div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")

    address_field.send_keys(all_addresses[n])
    price_field.send_keys(all_price[n])
    link_field.send_keys(all_links[n])

    time.sleep(2)
    submit_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/"
                                                  "div")
    submit_button.click()
