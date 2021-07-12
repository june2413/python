from EMP import EMP
from datetime import datetime

class EMPService:
    # 객체 생성없이 바로 사용가능한 static method로 선언
    @staticmethod
    def readEmp():          # 사원번호, 이름, 성, 이메일, 전화번호, 입사일 등 입력
        empno = input("사원번호를 입력하여 주십시오 : ")
        fname = input("이름을 입력하여 주십시오 : ")
        lname = input("성을 입력하여 주십시오 : ")
        email = input("이메일을 입력하여 주십시오 : ")
        phone = input("전화번호를 입력하여 주십시오 : ")
        hdate = input("입사일을 입력하여 주십시오 : ")

        return EMP(empno, fname, lname, email, phone, hdate)

    @staticmethod
    def computeDuty(emp: EMP):      # 입사일 기준 근무일 계산
        hdate = emp.hdate.split('-')

        now = datetime.now()
        hire = datetime(int(hdate[0]), int(hdate[1]), int(hdate[2])) # 연, 월, 일
        days = now - hire
        print(str(days).split()[0], '일')