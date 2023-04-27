# web2.py 
#웹서버와 통신 
import requests
#크롤링
from bs4 import BeautifulSoup

url = "https://www.daangn.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    title = post.find("h2", attrs={"class":"card-title"})
    price = post.find("div", attrs={"class":"card-price"})
    print("{0} , {1}".format(title, price))     # 하나의 문자열로 만들어서 출력한다.
    
    #ctrl + /:선택영역 주석처리 
    # <div class="card-desc">
    #       <h2 class="card-title">나이키 신발 팝니다!</h2>
    #       <div class="card-price ">
    #         10,000원
    #       </div>
    #       <div class="card-region-name">
    #         경기도 파주시 목동동
    #       </div>
