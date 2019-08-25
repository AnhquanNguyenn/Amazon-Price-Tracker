import requests
from bs4 import BeautifulSoup
from re import sub
from decimal import Decimal
import smtplib
import time

URL = 'https://www.amazon.com/Nikon-D750-FX-format-Digital-Camera/dp/B0060MVJ1Q/ref=sxin_3_osp48-fd978382_cov?ascsubtag=fd978382-76a6-478f-a63a-61423996920f&creativeASIN=B0060MVJ1Q&cv_ct_id=amzn1.osp.fd978382-76a6-478f-a63a-61423996920f&cv_ct_pg=search&cv_ct_wn=osp-search&keywords=Nikon+camera&linkCode=oas&pd_rd_i=B0060MVJ1Q&pd_rd_r=463bf9f3-27d0-463f-a9f6-b684dca04368&pd_rd_w=eUnoK&pd_rd_wg=sLFBn&pf_rd_p=01a10a0c-41cd-43e7-9966-cab0d3a2d561&pf_rd_r=Z80W0GDXA5SYDQM0QV2S&qid=1566758679&s=gateway&tag=spyonsite-20'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
    #print(soup.prettify())

    title = soup2.find(id='productTitle').get_text() 
    price = soup2.find(id='priceblock_ourprice').get_text()
    readable_price = price[0:9]
    converted_price = Decimal(sub(r'[^\d.]', '', readable_price))

    if (converted_price < 1400.00):
        send_email()

    print(title.strip())
    print(converted_price)

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('luckynguyen144@gmail.com', 'mknzjouhrhdwevkw')
    
    subject = 'Price Fell Down!'
    body = 'Check the amazon link \nhttps://www.amazon.com/Nikon-D750-FX-format-Digital-Camera/dp/B0060MVJ1Q/ref=sxin_3_osp48-fd978382_cov?ascsubtag=fd978382-76a6-478f-a63a-61423996920f&creativeASIN=B0060MVJ1Q&cv_ct_id=amzn1.osp.fd978382-76a6-478f-a63a-61423996920f&cv_ct_pg=search&cv_ct_wn=osp-search&keywords=Nikon+camera&linkCode=oas&pd_rd_i=B0060MVJ1Q&pd_rd_r=463bf9f3-27d0-463f-a9f6-b684dca04368&pd_rd_w=eUnoK&pd_rd_wg=sLFBn&pf_rd_p=01a10a0c-41cd-43e7-9966-cab0d3a2d561&pf_rd_r=Z80W0GDXA5SYDQM0QV2S&qid=1566758679&s=gateway&tag=spyonsite-20'
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'luckynguyen144@gmail.com', 
        'anhquan.nguyen5417@gmail.com',
        msg
    )
    print('Email has been sent!')
    server.quit()

while(True):
    check_price()
    time.sleep(60 * 60)