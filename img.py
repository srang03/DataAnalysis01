from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')
url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query=%EA%B3%A0%EC%96%91%EC%9D%B4&oquery=%EA%B0%95%EC%95%84%EC%A7%80&tqi=UI8z1wp0J14ssTq6mWNssssssmK-070763'

driver.get(url)
time.sleep(3) 

req = driver.page_source


soup = BeautifulSoup(req, 'html.parser')
pictures = soup.select('#_sau_imageTab > div > div > div > a > img')
#_sau_imageTab > div > div > div > a > img
# pictures = soup.select_one('#_sau_imageTab > div > div.photo_grid._box > div')

for i in pictures:
    print(i['src'])
driver.quit() 