sumAll = 0
answer = "yes"

while answer == "yes":
    number = int(input("수를 입력하세요: "))
    sumAll = sumAll + number
    ansver = input("계속할까요(yes/no)")
print("합계는",sumAll,"입니다.")
