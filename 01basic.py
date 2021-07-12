name = input('이름을 입력하세요.')
kor, eng, mat = map(int, input('국어, 영어, 수학점수를 입력하세요.').split())
tot = kor + eng + mat
avg = tot / 3

print(name)
print(kor)
print(eng)
print(mat)
print(tot)
print(avg)