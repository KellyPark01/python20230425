# web1.py
#크롤링을 위한 선언
from bs4 import BeautifulSoup

#페이지를 로딩(메서드 체인)
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read() # page : 문자열 변수
#검색이 용이한 객체 생성
soup = BeautifulSoup(page,"html.parser") # 일반적인 html 문서
print(soup.prettify())  # prettify : 문서를 그대로 보여줘