class BankAccount:
    """
    은행 계좌를 나타내는 클래스입니다.
    속성:
        __id (int): 계좌의 고유 식별자입니다.
        __name (str): 계좌 소유자의 이름입니다.
        __balance (float): 계좌의 현재 잔액입니다.
    메서드:
        deposit(amount): 지정된 금액을 계좌 잔액에 추가합니다.
        withdraw(amount): 지정된 금액을 계좌 잔액에서 빼냅니다.
        __str__(): 계좌 정보를 문자열 형태로 반환합니다.
    """

    def __init__(self, id, name, balance):
        """
        BankAccount 클래스의 새 인스턴스를 초기화합니다.
        매개변수:
            id (int): 계좌의 고유 식별자입니다.
            name (str): 계좌 소유자의 이름입니다.
            balance (float): 계좌의 초기 잔액입니다.
        """
        self.__id = id
        self.__name = name
        self.__balance = balance
    
    def deposit(self, amount):
        """
        계좌 잔액에 지정된 금액을 추가합니다.
        매개변수:
            amount (float): 입금할 금액입니다.
        """
        self.__balance += amount
    
    def withdraw(self, amount):
        """
        계좌 잔액에서 지정된 금액을 뺍니다.
        매개변수:
            amount (float): 출금할 금액입니다.
        """
        self.__balance -= amount
    
    def __str__(self):
        """
        계좌 정보를 문자열 형태로 반환합니다.
        반환값:
            str: 계좌의 식별자, 소유자 이름, 잔액을 포함하는 문자열입니다.
        """
        return "{0} , {1} , {2}".format(self.__id,
            self.__name, self.__balance)


if __name__ == "__main__":
    accounts = []
    for i in range(10):
        account = BankAccount(i, f"User{i}", i * 1000)
        account.deposit(500)
        account.withdraw(200)
        accounts.append(account)
    
    for account in accounts:
        print(account)