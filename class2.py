# class1.py
#1)클래스 정의
class Person:    
    def __init__(self):      # 클래스 틀 = 붕어빵 틀
        self.name = "default name"
        self.title = "default title"
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스 생성
p1 = Person()
p2 = Person()
p1.name = "전우치"  #name이라는 멤버변수에 전우치를 넣는다.

#런타임시에 변수 추가 (파이썬은 모호한 것보다는 명확한 것이 좋다.)
# Person.title = "new title"  #에러는 나지 않지만, class에 추가하는 것이 좋다.
# print(p1.title)
# print(p2.title)
# print(Person.title)


#3)메서드 호출
p1.print()    #함수가 아니고 메서드
p2.print()    #함수가 아니고 메서드