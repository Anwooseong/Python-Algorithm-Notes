L = int(input())
str = input()
sum = 0
M = 1234567891
for index, value in enumerate(str):
    sum += ((ord(value) - 96) * (31**index))
sum = sum % M
print(sum)