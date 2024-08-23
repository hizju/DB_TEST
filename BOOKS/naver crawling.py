from selenium import webdriver
from chromedriver_autoinstaller import install as install_chromedriver
from bs4 import BeautifulSoup
import time

# Chrome 웹 드라이버 설치 및 설정
driver = webdriver.Chrome()

# 교보문고 접속
url = f"https://product.kyobobook.co.kr/category/KOR/010315#?page=1&type=all&per=50&sort=new"
driver.get(url)

time.sleep(5)