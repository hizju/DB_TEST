from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

url = f"https://product.kyobobook.co.kr/category/KOR/010315#?page=1&type=all&per=50&sort=new"
driver = webdriver.Chrome()
driver.get(url)


# 교보문고의 베스트셀러 웹페이지를 가져옵니다.
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# li 태그 모두 가져오기
items = soup.select('.prod_item')

# 크롤링 해 온 데이터를 담을 배열
data = []

# 각 li 태그에서 책 정보 가져오기
for item in items:

    # # 책번호
    # link_number = item.find('a', class_="prod_link")['href'].split("/")[-1].strip()
    # 제목
    title = item.find('span', class_="prod_name").get_text(strip=True)
    labels = item.find('span', class_="prod_label")
    if labels is not None:
        for label in labels:
            title = title.replace(label.text.strip(), '')

    # # 작가
    # author = item.find('span', class_="prod_author").find('a').text.strip()
    # 책 소개
    # introduction = item.select_one('.prod_introduction').text.strip()
    # 가격
    price = item.find('div', class_="prod_price").find('span', class_="price").find('span', class_="val").text.strip()
    # 작가&출판사&출판년도
    company = item.find('span', class_="prod_author").text.strip()
    # # 출판년도
    # date = item.find('span', class_="prod_author").find('span', class_="date").text.strip()
    # 리뷰
    # review = item.select_one('.review_klover_text').text.strip()

    data.append((title, price, company))
    
# 데이터프레임 생성 후 CSV로 저장
df = pd.DataFrame(data, columns=['Title', 'Price', 'Company']) # 'Introduction', 'Review'
df.to_csv('books.csv', index=False)

# 드라이버 종료
driver.quit()
