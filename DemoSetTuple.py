# DemoSetTuple.py

print("---set형식---")
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print("---tuple형식---")
tp = (1,2,3)
print(type(tp))

#함수 정의
def calc(a,b):
    return a+b, a*b

print(calc(3,4))

print("id: %s, name: %s" % ("kim","김유신"))

args = (5,6)
print(calc(*args))

#디버깅 연습
def intersect(prelist, postlist):
    #교집합 문자를 모아둘 리스트 초기화 (지역변수)
    result = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        #x라는 글자가 postlist에 있고 a 아직 result에 없으면
        if x in postlist and x not in result:
            result.append(x)
    return result

#호출(디버깅시에 중단점)
print(intersect("HAM", "SPAM"))

#지역변수와 전역변수
#전역변수
x = 5
def func(a):
    return x+a

#호출
print(func(1))

def func2(a):
    #지역변수
    x = 10
    return x+a

#호출
print(func2(1))

#기본값
def times(a=10, b=20):
    return a*b

print( times() )
print( times(5) )
print( times(5,6) )

#키워드 인자 방식(인자, 파라메터명을 상세하게 기술)
def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

print(connectURI("credu.com", "80"))
print(connectURI(port="8080", server="credu.com"))

#선택한 행들을 주석처리 : ctrl + /
#print( dir() )
print( globals() )
