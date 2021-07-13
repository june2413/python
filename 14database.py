import sqlite3

# 데이터 조회
# 연결
conn = sqlite3.connect('C:/Java/sqlite3/yunbinni.db')

# 접속 후 커서를 가져옴
cur = conn.cursor()

# 쿼리 작성
sql = 'select pcode, pname, price, amount from product'

# 쿼리 결과집합 가져오기
cur.execute(sql)        # 실행
rows = cur.fetchall()   # 가져오기

# 리스트 내용 출력하기

for row in rows:
    print(row[0], row[1], row[2], row[3])
    # dictCursor : 컬럼명으로 리스트 출력함(단, sqlite3는 미지원)
    # print(row['pcode'], row['pname'], row['price'], row['amount'])

# 작업종료
cur.close()
conn.close()

########################################################################################################################
# mysql을 이용한 DB 활용하기
import pymysql

conn = pymysql.connect(host='bigdata.c0n0wa0hno7m.ap-northeast-2.rds.amazonaws.com', charset='utf8', user='yunbinni', password='dbsqls9049', db='playground')

cursor = conn.cursor(pymysql.cursors.DictCursor) # 커서 이름을 '키'형태로 불러올 수 있음

sql = 'select * from EMPLOYEES'

cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
    print(row['EMPLOYEE_ID'], row['FIRST_NAME'], row['LAST_NAME'])

# 직책이 IT_PROG인 사원들의 사번, 성, 입사일을 출력하는 코드 작성
sql = 'select EMPLOYEE_ID, LAST_NAME, HIRE_DATE from EMPLOYEES where JOB_ID = "IT_PROG"'

cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
    print(row['EMPLOYEE_ID'], row['LAST_NAME'], row['HIRE_DATE'])

# 30번 부서의 사원수를 조회하는 코드작성
sql = 'select count(*) from EMPLOYEES where DEPARTMENT_ID = 30'

cursor.execute(sql)
row = cursor.fetchone()

print(row)

# 이름, 국어, 영어, 수학을 입력받아 sungjuk 테이블에 저장
def newSungJuk() -> bool:
    conn = pymysql.connect(host='bigdata.c0n0wa0hno7m.ap-northeast-2.rds.amazonaws.com', charset='utf8', user='yunbinni', password='dbsqls9049', db='playground')
    cursor = conn.cursor()

    name = input("이름을 입력하여 주십시오 : ")
    kor = input("국어점수를 입력하여 주십시오 : ")
    eng = input("영어점수를 입력하여 주십시오 : ")
    mat = input("수학점수를 입력하여 주십시오 : ")

    sql = 'insert into sungjuk(name, kor, eng, mat) values(%s, %s, %s, %s)'

    cnt = cursor.execute(sql, (name, kor, eng, mat))
    conn.commit() # update, delete 시 commit 실행 필수

    cursor.close()
    conn.close()

    if cnt > 0:
        print("sungjuk테이블에 데이터 저장이 완료되었습니다.")
        return True
    else:
        print("저장에 실패하였습니다.")
        return False

newSungJuk()


cursor.close()
conn.close()

########################################################################################################################