# DemoForm2.py
# DemoForm2.ui(Qt디자이너에서 화면을 디자인한 파일) + DemoForm2.py(실제 로직이 저장됨)
import sys
from PyQt5.QtWidgets import *    # PyQt5.QtWidgets : PyQt5 패키지 안에 있는 QtWidgets 모듈의 모든 것을 impert한다.(PyQt는 클래스가 대문자 Q로 시작한다.)
from PyQt5 import uic

# 디자인한 파일을 로딩 : DemoForm.ui
form_class = uic.loadUiType("c:\\work\\DemoForm2.ui")[0]  # ui 태그는 일반적으로 1개이나 여러개가 나올 수 있으므로 슬라이싱 잘라서 쓸 수 있다.
# 윈도우(폼)클래스 정의(QMainWindow상속)
class DemoForm(QMainWindow, form_class):  # QMainWindow : 큰창
    def __init__(self):       # 초기화 메소드
        super().__init__()    # 다중 상속(부모가 여러개일 때)일 경우 super로 알아서 초기화해준다
        self.setupUi(self)
    def firstClick(self):
        self.label.setText("첫번째 버튼~~")  # 라벨에 문자열을 출력한다.
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭")  # 라벨에 문자열을 출력한다.
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭~~")  # 라벨에 문자열을 출력한다.       

#직접 모듈을 실행한 경우 인스턴스 생성
if __name__ == "__main__":   # 이 모듈을 직접 실행하였을 경우 (import 받아서 간접 수행한 것이 아니고)
    app = QApplication(sys.argv)  # 실행 프로세스 만들고
    demoForm = DemoForm()  # DemoForm을 초기화해서 인스턴스(복사본)를 만든다.
    demoForm.show()  # 화면을 보여준다
    app.exec_()  # 실행하면서 대기하다가 이벤트가 발생하면 실행한다.
