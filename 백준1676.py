def factorial(num, value):
    if num == 1 or num == 0:
        return 1
    else:
        return num * value


N = int(input())
count = 0
ans = 1
for i in range(N, -1 , -1):
    ans = factorial(i, ans)
    while ans%10 == 0:
        ans //= 10
        count += 1
print(count)