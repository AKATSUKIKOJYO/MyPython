names =[
            ["김유신","계백","을지문덕"],
            ["홍길동", "이순신","곽재우","권율"],
            ["김구","윤봉길","안창호","안중근"]
        ]
for name in names:
    for warrior in name:
        print(warrior)

for name in names[0]:
    print(name)
names.append(["강감찬","왕건","이성계"])
print(names)

print(names[-1])
print(names[0][0])
print(names[2][2])


names[-1][-1]="최무선"
print(names)

names.sort()
print(names)
