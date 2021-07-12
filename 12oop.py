# OOP의 캡슐화에 근거해서
# 객체명.속성으로 값을 수정하거나 읽는 것은 비추
# 이러한 작업은 setter, getter 메서드를 사용해야 함
# 접근제어 기능을 이용해서 '객체명.속성'으로는
# 수정/조회를 하지 못하게 하는 것이 좋음

class SungJuk2:
    def __init__(self, name, kor, eng, mat, tot=0, mean=0, grd='가'):
        # 멤버에 접근제한 기능 부여
        # 멤버명 앞에 __를 추가하면 private 멤버로 선언
        self.__name = name
        self.__kor = kor
        self.__eng = eng
        self.__mat = mat
        self.__tot = tot
        self.__mean = mean
        self.__grd = grd

    def __str__(self): # 멤버출력함수 = 매직함수
        result = f'{self.__name} {self.__kor} {self.__eng} ' \
                 f'{self.__mat} {self.__tot} {self.__mean} ' \
                 f'{self.__grd}'
        return result

    # getter, setter를 생성하는 방법
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    # Python스럽게 getter, setter를 생성하는 방법
    # @property, @setter, decorator(보조설명)
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def kor(self):
        return self.__kor

    @kor.setter
    def kor(self, kor):
        self.__kor = kor

    @property
    def eng(self):
        return self.__eng

    @eng.setter
    def eng(self, eng):
        return self.__eng

    @property
    def mat(self):
        return self.__mat

    @mat.setter
    def mat(self, mat):
        self.__mat = mat

    @property
    def tot(self):
        return self.__tot

    @tot.setter
    def tot(self, tot):
        self.__tot = tot

    @property
    def mean(self):
        return self.__mean

    @mean.setter
    def mean(self, mean):
        self.__mean = mean

    @property
    def grd(self):
        return self.__grd

    @grd.setter
    def grd(self, grd):
        self.__grd = grd

sj2 = SungJuk2('윤빈', 100, 100, 100)
# print(sj2.name) # __로 접근제어해서 오류가 난다.
print(sj2.getName())
print(sj2.name)

"""
DAO 클래스
Data Access Object
데이터베이스의 데이터에 접근하기 위한 역할 담당
MVC 패턴에서는 서비스클래스와 DAO 객체로
나눠 프로그래밍 함

DAO : 주로 DB를 사용해서 데이터를 조회하거나
조작하는 기능을 담당
서비스 : DB 작업전 데이터를 처리하는 기능을 담당
"""

class SungJuckService:
    def readSungJuk(self):
        name = input('이름은? ')
        kor = int(input('국어는? '))
        eng = int(input('영어는? '))
        mat = int(input('수학은? '))

        return SungJuk2(name, kor, eng, mat)

    def computeSungJuk(self, sj: SungJuk2):
        kor, eng, mat = sj.kor, sj.eng, sj.mat
        sj.tot = kor + eng + mat
        sj.mean = sj.tot / 3
        sj.grd = '가'
        if sj.mean >= 90:           sj.grd = '수'
        elif sj.mean >= 80:         sj.grd = '우'
        elif sj.mean >= 70:         sj.grd = '미'
        elif sj.mean >= 60:         sj.grd = '양'

    def printSungJuk(self, sj: SungJuk2):
        name, kor, eng, mat, tot, mean, grd = sj.name, sj.kor, sj.eng, sj.mat, sj.tot, sj.mean, sj.grd
        print('입력 : %s %d %d %d' % (name, kor, eng, mat))
        print('결과 : %d %.1f %s' % (tot, mean, grd))

    # CRUD
    def saveSungJuk(self):
        pass

    def readOneSungJuk(self):
        pass

    def readAllSungJuk(self):
        pass

    def modifySungJuk(self):
        pass

    def removeSungJuk(self):
        pass

sjsrv = SungJuckService()
sj = sjsrv.readSungJuk()
sjsrv.computeSungJuk(sj)
sjsrv.printSungJuk(sj)