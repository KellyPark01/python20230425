#정규표현식 사용
import re 

#로그파일
f=open('c:\\work\\PV3.txt','rt')  # 원본
g=open('c:\\work\\PV3_copy.txt','wt',encoding='utf-8')  # 복사본

#많은 라인의 파일이면 
#한번에 한줄씩 읽어서 처리한다.  
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f.readline()
while (line != ''):
    if (re.search("\d{4}", line)):  # 숫자 4자리가 연달아서 나오는 라인 찾아줘
#    if (re.search("error", line)):   # error가 있는지 찾아라
        g.write(line + "\n")         # 검색한 라인을 복사본에 저장해서 만들어줘
    line = f.readline()

f.close() 
g.close()








