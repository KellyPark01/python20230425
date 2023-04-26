# db1.py
import sqlite3

#연결객체를 생성(메모리에서 연습)
con = sqlite3.connect(":memory:")
#SQL 구문을 실행할 커서객체
cur = con.cursor()
#테이블 구조(스키마) 생성
cur.execute("create table if not exists PhoneBook " + 
    " (id integer primary key autoincrement, name text, phoneNum text);")  #id 컬럼이름, 정수, PK 속성을 주고, 자동증가속성 autoincrement,,, text : 문자열 str과 동일
#1건입력
cur.execute("insert into PhoneBook (name, phoneNum) values " + 
    " ('홍길동', '010-111-1234');")  # 문자열 인식을 위해서 밖을 쌍따옴표로 적음
#검색
cur.execute("select * from PhoneBook;")
for row in cur:   # 커서 인스턴스에서 
    print(row)    # 결과  (1, '홍길동', '010-111-1234')
