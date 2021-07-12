for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} X {j} = {i * j:2d} \t", end='')
    print()

# 트리
n = int(input())

for i in range(1, n + 1):
    print(' '*(n - i), end='')
    print('*'*(2*i - 1))

# 트리(다른 풀이)
n = int(input())

for i in range(n):
    for j in range(n - 1 - i):
        print(' ', end='')
    for k in range(2*i + 1):
        print('*', end='')
    print()

# 369
for i in range(1, 100):
    print(i, end=' ')
    for j in str(i):
        if j in ['3', '6', '9']:
            print("짝!", end=' ')
    print()

# 열차충돌
a_h, a_m = 9, 0
aData = []
b_h, b_m = 9, 0
bData = []
c_h, c_m = 9, 0
cData = []

while True:
    a_m += 10 ; b_m += 25 ; c_m += 30
    if a_m >= 60:
        a_h += 1
        a_m -= 60
    if b_m >= 60:
        b_h += 1
        b_m -= 60
    if c_m >= 60:
        c_h += 1
        c_m -= 60
    aData.append((a_h, a_m))
    bData.append((b_h, b_m))
    cData.append((c_h, c_m))

    if a_h >= 18 and b_h >= 18 and c_h >= 18:
        break