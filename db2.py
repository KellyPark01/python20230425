# db2.py
import sqlite3

#연결객체를 생성(물리적인 파일에 저장)
con = sqlite3.connect("c:\\work\\sample.db")  # db1.py와 다른 점
#SQL 구문을 실행할 커서객체
cur = con.cursor()
#테이블 구조(스키마) 생성
cur.execute("create table if not exists PhoneBook " + 
    " (id integer primary key autoincrement, name text, phoneNum text);")  #id 컬럼이름, 정수, PK 속성을 주고, 자동증가속성 autoincrement,,, text : 문자열 str과 동일
#1건입력
cur.execute("insert into PhoneBook (name, phoneNum) values " + 
    " ('홍길동', '010-111-1234');")  # 문자열 인식을 위해서 밖을 쌍따옴표로 적음
#입력 파라메터 처리
name = "이순신"
phoneNumber = "010-222-1234" 
cur.execute("insert into PhoneBook (name, phoneNum) values " + 
    " (?, ?);", (name, phoneNumber))  # ? 이자리에 나중에 변수 값이 올거야. replace  ( 튜플로 묶어서 한방에 넣는다.)
#다중위 데이터를 입력(2차원 배열)
datalist = (("전우치", "010-333-1234"), ("박문수", "010-123-5678"))  # 밖의 튜플 안에 또 튜플을 넣음, 2개의 레코드가 튜플 안에 튜플로 들어가 있다.
cur.executemany("insert into PhoneBook (name, phoneNum) values " +   # 1번 수행이 아니고 2번 수행이므로 executemany 사용함
    " (?, ?);", datalist)  

#검색
cur.execute("select * from PhoneBook;")
#for row in cur:   # 커서 인스턴스에서 
#    print(row)    # 결과  (1, '홍길동', '010-111-1234') (2, '이순신', '010-222-1234') (3, '전우치', '010-333-1234') (4, '박문수', '010-123-5678')
print("---fetchone()---")
print(cur.fetchone())        # 보여주고 사라진다. 
cur.execute("select * from PhoneBook;")   # 전체를 다시 보여주고 싶으면 다시 조회해서 버퍼를 채워주고 검색한다.
print("---fetchmany(2)---")
print(cur.fetchmany(2))
print("---fetchall()---")
cur.execute("select * from PhoneBook;") 
print(cur.fetchall())  # 버퍼 메모리에 남아있는 데이터만 조회된다.
#작업 정상 종료
con.commit()


#파이썬 아이들에서 실행해보자
#import sqlite3 
#con = sqlite3.connect("c:\\work2\\test.db") 
#cur = con.cursor()
#cur.execute("select * from PhoneBook;")
#cur.fetchall()   #커밋이 되면 전체 데이터가 조회된다.
