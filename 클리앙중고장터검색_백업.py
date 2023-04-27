# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) - 헤더를 넣어줘서 웹봇이 아니라고 속인다.
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

#페이지 주소를 0부터 9까지 생성 ( 페이지 주소를 보고 파악해야함 )
for n in range(0,10):  # 0부터 9까지의 정수를 만들어준다. 규칙이 있는 수열이므로 range 사용
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)   # &po= : 페이지 번호 &po=0 는 1페이지
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()   # data : 문자열 변수
        #한글이 깨지는 경우 다시 해석
        page = data.decode('utf-8', 'ignore')  # data는 문자열 변수, utf-8 : 유니코드로 다시 해석, ignore : 글자가 깨져도 상관없다. 
        #2300줄 문자열 넘기는 코드
        soup = BeautifulSoup(page, 'html.parser') # html.parser : 인터넷 페이지
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})   # span 태그 중에서 속성이 data-role = list-title-text 인거 찾기
        # 크롬 브라우저 우측 상단 점 3개 -> 도구더보기 -> 개발자도구 누르고 오른쪽 상단에 네모박스에 화살표 누르기
        # <span class="subject_fixed" data-role="list-title-text" title="아이패드 9세대 64GB 셀룰러 LTE 단순개봉 새제품급 판매합니다.">
        # 	아이패드 9세대 64GB 셀룰러 LTE 단순개봉 새제품급 판매합니다.
        # </span>        
        for item in list:
                # try:    # 시도해보고 에러가 나면 나가라 ( try : 에러 처리하는 키워드)
                #         title = item.text.strip()  # 태그는 제외하고 공백 제거
                #         print(title)
                #         # if (re.search('아이폰', title)):
                #         #         print(title.strip())
                # except:
                #         pass
                title = item.text.strip()  # 태그는 제외하고 공백 제거
                #print(title)
                if (re.search('애플워치', title)):   # re.search : 끝까지 지독하게 검색한다. ( 애플워치만 보여줌 )
                        print(title)
