# web1.py
#크롤링을 위한 선언
from bs4 import BeautifulSoup

#페이지를 로딩(메서드 체인)
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read() # page : 문자열 변수
#검색이 용이한 객체 생성
soup = BeautifulSoup(page,"html.parser") # 일반적인 html 문서  sopu이라는 인스턴스 복사본 찍음
#print(soup.prettify())  # prettify : 문서를 그대로 보여줘
#<p>태그 전부 검색
#print(soup.find_all("p")) # "p" : P태그 : <p> ,  find_all : 메서드
#<p>하나만 검색
#print(soup.find("p"))  # <p> 태그 하나만 보여줘
#<p class="outer-text">
#print(soup.find_all("p", class_="outer-text"))  # 필터링(class_="outer-text" 속성을 가지고 있는 P태그를 보여줘), class는 파이썬의 키워드 이므로 class뒤에 언더바 _ 붙임
#print(soup.find_all("p", attrs={"class":"outer-text"})) # p태그 중에 클래스 속성이 outer-text 인 것을 가져와라
#태그 내부에 컨텐츠만 사용
for item in soup.find_all("p"):
    #태그는 버리고 컨텐츠만 사용
    title = item.text.strip()   # 태그는 빠지고 item.text.strip 공백을 지우고 안쪽의 컨텐츠만 가져와라
    title = title.replace("\n", "")  # 줄바꿈 문자가 나오면 지워라
    print(title)




