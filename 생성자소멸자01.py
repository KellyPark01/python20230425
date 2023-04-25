# -*- 생성자와 소멸자 -*-
class MyClass:
    #가장 먼저 실행되는 초기화 메서드(생성자)
    def __init__(self, value):
        self.value = value
        print("Instace is created! value = ", value)
    #가장 마지막에 인스턴스를 소멸하면서 실행되는 메서드(소멸자)
    def __del__(self):
        print("Instance is deleted!")

#인스턴스 생성
m = MyClass(5)
#del m  # MyClass 클래스 만들고 m 인스턴스 만든 다음 다 쓴 후에 삭제한다. (반드시 삭제하지 않아도 된다. 자동으로 GC가 가지비를 정리해준다.)

print("전체 코드 실행 종료")