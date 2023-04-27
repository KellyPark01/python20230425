# DemoForm.py
# DemoForm.ui(Qt디자이너에서 화면을 디자인한 파일) + DemoForm.py(실제 로직이 저장됨)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 디자인한 파일을 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]  # ui 태그는 일반적으로 1개이나 여러개가 나올 수 있으므로
# 윈도우(폼)클래스 정의
class DemoForm(QDialog, form_class):
    def __init__(self):       # 초기화 메소드
        super().__init__()    
        self.setupUi(self)
        self.label.setText("첫번째 화면~~")

#직접 모듈을 실행한 경우 인스턴스 생성
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()  # 실행하면서 대기하다가 이벤트가 발생하면 실행한다.
