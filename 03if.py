print("속도 위반!!" if int(input()) > 50 else "")

print("팬(Fan) 가동" if int(input("기계 온도를 입력하세요.")) >= 40 else "팬(Fan) 중지")

print("안녕하세요.\n"*100)

print(*[i for i in range(1, 101) if i%3==0 and i%8==0])