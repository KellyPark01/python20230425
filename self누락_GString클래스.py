#전역변수
str = "Not Class Member"
#클래스 정의
class GString:
    def __init__(self):
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #버그
        print(self.str)  #원래 코드 print(str)      

#인스턴스 생성
g = GString()
g.set("First Message")
g.print()
