# function1.py
#1)함수 정의
def times(a,b):
    return a*b

#2) 함수 호출
result = times(3,4)
print(result)

def setValue(newValue):
    #지역변수
    x = newValue
    print("함수내부:", x)

#호출
retValue = setValue(5)
print(retValue)

def swap(x,y):
    return y,x

#호출
print(swap(3,4))

