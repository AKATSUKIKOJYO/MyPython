n = 1234
sum = 0
while n>0:
    digit = n%10
    sim = sum+digit
    n = n//10
print(sum)
