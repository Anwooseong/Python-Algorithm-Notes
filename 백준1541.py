arr = list(map(str, input().split('-'))) #55-50+40 -> [55, 50+40]

for i in range(len(arr)):
    sum = 0
    div = arr[i].split('+')
    for j in div:
        sum += int(j)
    arr[i] = sum
for i in range(len(arr)):
    arr[i] = int(arr[i])
ans = arr[0]
for i in range(1, len(arr)):
    ans -= arr[i]
print(ans)