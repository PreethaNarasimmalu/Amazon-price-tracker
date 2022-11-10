import requests
# import bs4
from bs4 import BeautifulSoup
import smtplib
import html

AMAZON_URL = "https://www.amazon.in/Instant-Pot-Duo-Multi-Functional-Pressure/dp/B01NBKTPTS/?_encoding=UTF8&pd_rd_w=F8jWY&content-id=amzn1.sym.7f5c9a81-22bb-4bd0-ab0e-f502d7e89ce7&pf_rd_p=7f5c9a81-22bb-4bd0-ab0e-f502d7e89ce7&pf_rd_r=53HE970EZT8QY4EFHYTK&pd_rd_wg=sq8Ji&pd_rd_r=0df005cf-d644-4809-9021-86af3c153383&ref_=pd_gw_unk"
MY_EMAIL = YOUR_EMAIL
MY_PASSWORD = YOUR_PSWD
BUY_PRICE = 10000

Headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Connection": "keep-alive"
}

response = requests.get(url=AMAZON_URL, headers=Headers)

content=response.text

soup = BeautifulSoup(content, "html.parser")

product_data = soup.find(name="span", id="productTitle")
price_data = soup.find(name="span", class_="a-offscreen")

product_title = html.escape(product_data.getText().strip())
price = int(price_data.getText().split("₹")[1].replace(',',"").split('.')[0])

message = f"{product_title} is now available at ₹{price}\n{AMAZON_URL}".encode('ascii', 'ignore')
if price < BUY_PRICE :
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Amazon Price Alert !!\n\n{message}"
        )
