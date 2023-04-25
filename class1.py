# class1.py
#1)클래스 정의
class Person:    
    def __init__(self):      # 클래스 틀 = 붕어빵 틀
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스 생성
p1 = Person()
p2 = Person()
p1.name = "전우치"  #name이라는 멤버변수에 전우치를 넣는다.

#3)메서드 호출
p1.print()    #함수가 아니고 메서드
p2.print()    #함수가 아니고 메서드