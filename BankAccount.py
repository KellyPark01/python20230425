# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        #인스턴스 멤버 변수
        #클래스 내부에 변수명 숨김
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):  # 입금
        self.__balance += amount 
    def withdraw(self, amount):  # 출금
        self.__balance -= amount
    def __str__(self):    #개발자가 원하는 문자열 출력
        # \ 는 하나의 라인으로 붙여서 본다. return "{0} , {1} , {2}".format(self.__id, self.__name, self.__balance)
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)

print(account1)
print(account1._BankAccount__balance)  #이런 규칙으로 사용하면 백도어로 확인은 가능하다.