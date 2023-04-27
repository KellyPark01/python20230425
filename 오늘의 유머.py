# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) - 헤더를 넣어줘서 웹봇이 아니라고 속인다.
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

#mode: append + read + write ()
f = open("c:\\work\\humor.txt", "a+", encoding="utf-8")  # wt : write text, 유니코드로 인코딩 ( a+ : 파일을 첨부)
#페이지 주소를 1부터 10까지 생성 ( 페이지 주소를 보고 파악해야함 )
for n in range(1,11):  # 1부터 10까지의 정수를 만들어준다. 규칙이 있는 수열이므로 range 사용 ( 10 + 1)
        #클리앙의 중고장터 주소 
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)   # &page= : 페이지 번호 &page=1 는 1페이지
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()   # data : 문자열 변수
        #한글이 깨지는 경우 다시 해석
        page = data.decode('utf-8', 'ignore')  # data는 문자열 변수, utf-8 : 유니코드로 다시 해석, ignore : 글자가 깨져도 상관없다. 
        #2300줄 문자열 넘기는 코드
        soup = BeautifulSoup(page, 'html.parser') # html.parser : 인터넷 페이지
        list = soup.find_all('td', attrs={'class':'subject'})   # td 태그 중에서 속성이 class = subject 인거 찾기
       
        # 크롬 브라우저 우측 상단 점 3개 -> 도구더보기 -> 개발자도구 누르고 오른쪽 상단에 네모박스에 화살표 누르기 태그 복사해오기
        #<td class="subject">
        # a href="/board/view.php?table=bestofbest&amp;no=467353&amp;s_no=467353&amp;page=1" target="_top">전세사기 대안 근황</a><span class="list_memo_count_span"> [32]</span>  <span style="margin-left:4px;"><img src="http://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span><img src="http://www.todayhumor.co.kr/board/images/list_icon_shovel.gif?2" alt="펌글" style="margin-right:3px;top:2px;position:relative"> </td>    
        for item in list:
            title = item.find("a").text.strip()  # a 태그를 찾아서 태그 제거 공백 제거
            #print(title)
            if (re.search('한국', title)):   # re.search : 끝까지 지독하게 검색한다. ( 한국 단어가 제목에 포함된 게시글을 보여줌 )
                print(title)
                f.write(title + "\n")

f.close()      # 루프가 끝나면 파일 닫고 나와라                  
