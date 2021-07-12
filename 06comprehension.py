print("\n".join(["*"*i for i in range(1, int(input()) + 1)]))

[i*2 for i in range(0, 11)]
[i**2 for i in range(1, 11)]

["even" if i % 2 == 0 else "odd" for i in range(1, 101)]

[f"{dan} X {num} = {dan * num}" for dan in range(7, 9) for num in range(1, 10)]

from math import sqrt

[i for i in range(1, 101) if sqrt(i) != int(sqrt(i))]

bloods = []
for i in range(10):
    blood = input("헌혈해주셔서 감사합니다.\n혈액형을 선택하세요 (A, B, AB, O)")
    bloods.append(blood)

print('-'*30)
print('혈액형 수급 현황')
print('-'*30)

