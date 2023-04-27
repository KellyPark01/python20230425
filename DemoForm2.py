# DemoForm2.py
# DemoForm2.ui(Qt디자이너에서 화면을 디자인한 파일) + DemoForm2.py(실제 로직이 저장됨)
# 사용하는 라이브러리에 대한 선언부
# 선언이 필요한 부분 추가하기
import sys
from PyQt5.QtWidgets import *    # PyQt5.QtWidgets : PyQt5 패키지 안에 있는 QtWidgets 모듈의 모든 것을 impert한다.(PyQt는 클래스가 대문자 Q로 시작한다.)
from PyQt5 import uic
#웹서버와 통신 
import requests #웹서버에 요청할 수 있는 라이브러리 요청
#크롤링
from bs4 import BeautifulSoup  #BeautifulSoup 모듈

# 디자인한 파일을 로딩 : DemoForm.ui
form_class = uic.loadUiType("DemoForm2.ui")[0]  # ui 태그는 일반적으로 1개이나 여러개가 나올 수 있으므로 슬라이싱 잘라서 쓸 수 있다. (경로를 써줘도 된다)
# 윈도우(폼)클래스 정의(QMainWindow상속)
class DemoForm(QMainWindow, form_class):  # QMainWindow : 큰창
    def __init__(self):       # 초기화 메소드
        super().__init__()    # 다중 상속(부모가 여러개일 때)일 경우 super로 알아서 초기화해준다
        self.setupUi(self)

    # 슬롯부분을 추가한다.    
    def firstClick(self):  # 첫번째 버튼을 누르면 처리되는 슬록 부분
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
        self.label.setText("당근마켓에서 크롤링 완료")  # 라벨에 문자열을 출력한다.
    def secondClick(self):  # 두번째 버튼을 누르면 처리되는 슬록 부분
        self.label.setText("두번째 버튼을 클릭")  # 라벨에 문자열을 출력한다.
    def thirdClick(self):   # 세번째 버튼을 누르면 처리되는 슬록 부분
        self.label.setText("세번째 버튼을 클릭~~")  # 라벨에 문자열을 출력한다.       

#직접 모듈을 실행한 경우 인스턴스 생성
if __name__ == "__main__":   # 이 모듈을 직접 실행하였을 경우 (import 받아서 간접 수행한 것이 아니고)
    app = QApplication(sys.argv)  # 실행 프로세스 만들고
    demoForm = DemoForm()  # DemoForm을 초기화해서 인스턴스(복사본)를 만든다.
    demoForm.show()  # 화면을 보여준다
    app.exec_()  # 실행하면서 대기하다가 이벤트가 발생하면 실행한다.
