from bs4 import BeautifulSoup
import lxml
import requests
import smtplib

website_endpoint = ("https://www.amazon.co.uk/MSI-GeForce-VENTUS-Gaming-Graphics/dp/B08Z83QKWX/ref=sr_1_2?c=ts&keywords"
                    "=Graphics%2BCards&s=computers&sr=1-2&ts_id=430500031&th=1")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 "
                 "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.6"
}

EMAIL_ID = "your Email here"
PASSWORD = "Your Password here"

response = requests.get(website_endpoint, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.content, "lxml")

price_whole = soup.find("span", class_="a-price-whole")
price_fraction = soup.find("span", class_="a-price-fraction")
price_total = float(price_whole.getText()) + (float(price_fraction.getText())/100)

title = soup.find("span", id="productTitle", class_="a-size-large product-title-word-break").getText(strip=True)

buy_price = 269.80

if price_total < buy_price:
    message = f"{title} is now {price_total}."

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        result = connection.login(EMAIL_ID, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ID,
            to_addrs=EMAIL_ID,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{website_endpoint}".encode("utf-8")
        )
        
