# function2.py
#가변인자(*sms Tuple을 의미)
def union(*ar):
    #지역변수 리스트에 문자 모으기
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출
print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))

#람다함수
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))

print((lambda x:x*x)(4))

print(globals())
