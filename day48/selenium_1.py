from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.flipkart.com/apple-iphone-14-pro-max-gold-128-gb/p/itm898d084d8a65f?pid=MOBGHWFHGDS3H5S9&lid=LS"
           "TMOBGHWFHGDS3H5S9AM0G7C&marketplace=FLIPKART&q=iphone+14+pro+max&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_5_7_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_5_7_na_na_na&fm=organic&iid=e5c72031-fa3d-412d-bb97-79ae75a62615.MOBGHWFHGDS3H5S9.SEARCH&ppt=hp&ppn=homepage&ssid=lk8v4dek3k0000001693371218494&qH=37e37d60a349d989")

price_inr = driver.find_element(By.CLASS_NAME, "_30jeq3").text
price_npr = float(price_inr.replace("₹","").replace(",","")) * 1.6
print(f"Total Nepali price for Iphone 14 pro max is {price_npr:.2f}")
