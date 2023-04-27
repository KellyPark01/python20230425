# web2.py 
#웹서버와 통신 
import requests #웹서버에 요청할 수 있는 라이브러리 요청
#크롤링
from bs4 import BeautifulSoup  #BeautifulSoup 모듈

url = "https://www.daangn.com/"  # 당근마켓 문자열 변수url에 담아서
response = requests.get(url)     # 요청 후 response 문자열로 받음
soup = BeautifulSoup(response.text, "html.parser")   # soup이라는 객체를 보낸다

posts = soup.find_all("div", attrs={"class":"card-desc"})  # find_all 전부 다 가져와 div인데 속성이 class가 card-desc 인거 
#파일에 저장
f = open("c:\\work\\daangn.txt", "wt", encoding="utf-8")   # open 함수를 사용해서 파일로 떨군다.
for post in posts:
    title = post.find("h2", attrs={"class":"card-title"})
    price = post.find("div", attrs={"class":"card-price"})
    title = title.text.replace("\n", "") # \n이 있으면 공백 제거
    price = price.text.replace("\n", "")    
    #print("{0} , {1}".format(title.text, price.text))     # 하나의 문자열로 만들어서 출력한다. .text (속성)를 붙인 이유는 앞뒤의 태그를 제거하고 안에 있는 컨텐츠만 보여주기 위함
    print("{0} , {1}".format(title, price))  
    result = f"매물: {title} 가격: {price} \n"   # 
    f.write(result)

f.close()  # for 루프 끝나고 파일 닫기

    #ctrl + /:선택영역 주석처리 
    # <div class="card-desc">
    #       <h2 class="card-title">나이키 신발 팝니다!</h2>   # h2 태그는 1개이다.클래스 속성이 card-title이다.
    #       <div class="card-price ">
    #         10,000원
    #       </div>
    #       <div class="card-region-name">
    #         경기도 파주시 목동동
    #       </div>
