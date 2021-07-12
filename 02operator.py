sales = []
for i in range(3):
    sales.append(int(input(f'{i + 1}월 매출을 입력해주세요.')))

print(f"1분기 전체 매출 : {sum(sales)}")

##############################################################
sales = int(input("1분기 매출 : "))
purchase = int(input("1분기 매입 : "))
print(f"수익 : {sales - purchase}원")

##############################################################
print("True" if 120 <= int(input('어린이의 신장을 입력하세요. ')) < 170 else "False")

##############################################################
name = input('이름을 입력하세요')
score = list(map(int, input('국어, 영어, 수학 점수를 입력하세요.').split()))

print(sum(score))
print(score/3)

num = int(input())
print("\n".join(["%d x %d = %2d" % (num, i, num * i) for i in range(1, 10)]))