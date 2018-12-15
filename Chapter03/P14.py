number = int(input("정수를 입력하시오: "))
num1000 = number // 1000
num100 = (number % 1000) // 100
num10 = (number % 100) // 10
num1=  number % 10
print("자릿수의 합: ", num1000 + num100 + num10 + num1)
