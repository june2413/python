hobbies = ['독서', '등산', '요리']
hobbies.append('배구')

# 합격 여부 판정하기
data = list(map(int, input().split()))
under40 = 0
avg = 0

for i in data:
    if i < 40 : under40 += 1
avg = sum(data) / len(data)

print(f"40점 미만 과목수 : {under40}")
print(f"평균 점수 : {avg}")
print("축하합니다. 합격하셨습니다." if avg >= 60 and under40 == 0 else "아쉽습니다. 불합격하셨습니다.")

# 모의고사 높은 성적순으로 정렬하기
data = [90, 100, 88, 85, 95, 92, 70, 75, 100, 92, 78, 80, 75, 95, 90, 100, 84]

data.sort()
data

for i in range(len(data)//2):
    data[i], data[len(data) - i - 1] = data[len(data) - i - 1], data[i]

data

# 함수를 이용한 다른 풀이
print(sorted(data, reverse=True))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
alphabet[3::-1]