# DemoRandom.py
#상단 모듈에 대한 선언
import random
from os.path import *   # from은 생략하겠다.
from os import *
import glob

print( random.random() )
print( random.random() )
print( random.uniform(2.0, 5.0) )
#리스트 컴프리헨션(내장)
print( [random.randrange(20) for i in range(10)] )  # 0~19까지 10개만 뽑음, 중복 가능
print( [random.randrange(20) for i in range(10)] )
print( random.sample(range(20), 10))                # 0~19까지 10개만 뽑음, 중복 없는 유니크한 값
print( random.sample(range(20), 10))

print("---파일 정보---")
print( abspath("python.exe") )  # 전체 풀 경로
print( basename("c:\\python310\\python.exe") )  # 해당 경로에 있는 파일 명만 반환
if exists("c:\\python310\\python.exe"):
    print( getsize("c:\\python310\\python.exe") )
else:
    print("파일 없음")

#특정 파일을 실행
#system("notepad.exe")             # 노트패드 앱이 실행된다. ( 계속 실행되니까 주석처리 함)

print("운영체제이름:{0}".format(name))    # 운영체제이름:nt  (윈도우)

lst = glob.glob("c:\\work\\*.py")  # 해당 경로의 모든 파일의 확장자가 py인 파일을 가져와라 ( 리스트 구조로 리턴된다 )
#print(lst)
for item in lst:    # 파일 목록을 보여준다.
    print(item)








