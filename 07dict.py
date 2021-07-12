data = {"C/C++" : "A",
        "Java" : "B+",
        "모바일" : "C",
        "보안" : "A+",
        "해킹" : "F",
        "시스템" : "C+"}

print(data["Java"])
print(data["시스템"])

data["파이썬"] = "A"
data["OS"] = "A+"

data["Java"] = "F"
data["시스템"] = "A"

a = [1, 3, 5]
b = [2, 4, 6]

[i + j for i, j in zip(a, b)]