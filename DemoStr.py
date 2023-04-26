# DemoStr.py

#print(dir(str))

strA = "파이썬은 강력해"
strB = "python is very powerful"
print(len(strA)) # 길이
print(len(strB))
print(strB.capitalize()) # 첫글자를 대문자로 변환
print(strB.count("p"))   # p가 몇번 나오는지
print(strB.startswith("pyt"))
print(strB.endswith("ful"))
print(strB.upper())
print("MBC2580".isalnum())   # 알파벳과 숫자
print("MBC:2580".isalnum())  # 중간에 문자 : 가 포함되어서 Faluse 반환함
print("2580".isdecimal())

data = "<<< spam and ham >>>"
result = data.strip("<> ")
print(data)
result = result.replace("spam", "spam egg")  # 치환한다. 꼭 리턴 받아야함
print(result)
lst = result.split()  # 자르기
print(lst)
print("---다시 하나의 문자열---")
print(":)".join(lst))  #합치기
