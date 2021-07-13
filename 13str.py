ss = '파이썬은완전재미있어요'

print(''.join([ss[i] if i%2==0 else "#" for i in range(len(ss))]))

str = "파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠 ^^"
str.count("공부")
str.find("공부") # 없는 문자열을 입력할 경우, -1 반환
str.index("공부") # 없는 문자열을 입력할 경우, error 발생
str.rfind("공부") # 뒤에서부터 찾는다.

str.startswith("파이썬")
str.endswith("^^")

# 공백다루기(또는 특정문자 제거)
str = ' 파 이 썬 '
str.strip()
str.lstrip()
str.rstrip()

str = ' 파 이 썬 '
str.replace(' ', '')

str = '--파---이---썬--'
str.replace('-', '')

str = '<< 파 << 이 >> 썬 >>'
str = str.replace('<', '')
str = str.replace('>', '')
str = str.replace(' ', '')