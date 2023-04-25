# DemoFile.py
#쓰기(유니코드방식으로 쓰기)
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8") #안전하게 인코딩 방식 지정
f.write("첫번째\n두번째\n세번째\n") #\n 줄바꾸기
f.close()

#읽기
f = open(r"c:\work\demo.txt", "rt", encoding="utf-8") #안전하게 인코딩 방식 지정
result = f.read()
print(result)
f.close()
