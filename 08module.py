# 패키지 package
# 함수, 클래스들을 용도별로 분리해서
# 작성하는 것을 모듈이라 했음

# 그런데, 이러한 모듈들이 모여 뒤죽박죽 섞여 있으면
# 이해도, 활용도가 떨어질수 있음

# 따라서, 모듈들 역시 성격에 맞게 분류해서 관리해야 할
# 필요성이 대두 - 패키지를 이용해서 모듈들을 관리

# 파이썬에서는 패키지를 만들려면
# 디렉토리 생성 -> __init__.py 파일 생성하면 됨
# python3 이상 __init__.py 를 만들지 않아도
# 패키지로 인식
# => python2와의 호환을 위해 생성할 것을 권장

import module.calculator

module.calculator.add(3, 5)

import module.ConvertUnit

data = int(input('변환할 길이(mm)를 입력하세요'))

result = module.ConvertUnit.convertLength(data)
module.ConvertUnit.convertLength(data)

import module.exam

module.exam.exampass()

import time as t
print(t.time())
print(t.localtime()) # tm_wday 주의

fmt = '%Y-%m-%d %H:%M:%S'
print(t.strftime(fmt, t.localtime()))

print('3초후에 다음 메시지가 출력됩니다.')
t.sleep(3)
print('하이')

""" 로또 당첨 프로그램 """
import random

myLotto = list(map(int, input("이번 주 나의 로또 번호는?").split()))
Lotto = []
ilchi = []
bulilchi = []

# 로또번호 추출
while len(Lotto) < 6:
    num = random.randrange(1, 46)
    if num not in Lotto:
        Lotto.append(num)

Lotto.sort()

for i in myLotto:
    if i in Lotto : ilchi.append(i)
    else : bulilchi.append(i)

ilchi.sort()
bulilchi.sort()

print(f"이번 주 로또 번호 : {Lotto}")
print(f"일치 번호 : {ilchi}")