# DemoRE.py
import re 

#함정을 추가
result = re.search("[0-9]*th", "  35th")  # 숫자가 출현횟수가 0번 나오고 th 나오는 거, 앞에 공백이 있어도 검색이 가능함
print(result)          # <re.Match object; span=(0, 4), match='35th'>    
print(result.group())  # 찾은 결과만 리턴  <re.Match object; span=(0, 4), match='35th'>   #  35th

# result = re.match("[0-9]*th", "  35th")   # 정확한 값을 찾지 못해서 에러남
# print(result)
# print(result.group())

result = re.search("apple", "this is apple")
print(result.group()) 
result = re.search("\d{4}", "올해는 2023년입니다.")  # 숫자가 연속으로 4자리
print(result.group()) 
result = re.search("\d{5}", "우리 동네는 52300")  # 숫자가 연속으로 5자리 나오면 
print(result.group()) 