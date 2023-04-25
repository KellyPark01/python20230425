# DemoLoop.py
value = 5
while value > 0:
    print(value)
    value -= 1

lst = [100,200,300]
fruit = {"apple":100, "kiwi":200}
for item in fruit.items():
    print(item)

print("---break구문---")
lst = list(range(1,11))
for i in lst:
    #선택 라인 주석 : ctrl + /
    if i > 5:
        break
    print("Item:{0}".format(i))

print("---continue구문---")
lst = list(range(1,11))
for i in lst:
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))


print("---range()함수---")
print(list(range(2000,2024)))
print(list(range(1,32)))
lst = list(range(1,11))
print("---리스트 컴프리핸션---")
print([i**2 for i in lst if i > 5])
fruits = {100:"apple", 200:"orange"}
print([v.upper() for v in fruits.values()])

print("---필터링없음---")
lst = [10, 25, 30]
itemL = filter(None, lst)
for i in itemL:
    print(i)

print("---필터링함수---")
lst = [10, 25, 30]
def getBiggerThan20(i):
    return i > 20

itemL = filter(getBiggerThan20, lst)
for i in itemL:
    print(i)

print("---람다함수---")  # 람다함수 : 한번쓰고 버리는 함수
lst = [10, 25, 30]

itemL = filter(lambda x:x>20, lst)
for i in itemL:
    print(i)