def exampass():
    a = int(input("1과목 점수를 입력하세요."))
    b = int(input("2과목 점수를 입력하세요."))
    c = int(input("3과목 점수를 입력하세요."))

    tot = a + b + c
    avg = tot/3
    print(f"총점 : {tot}")
    print(f"평균 : {avg}")
    print(f"합격여부 : {'Pass' if avg >= 60 and a >= 40 and b >= 40 and c >= 40 else 'Fail'}")