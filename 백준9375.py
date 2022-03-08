test = int(input())
for _ in range(test):
    n = int(input())
    if n == 0:
        print('0')
        continue
    dict = {}
    for i in range(n):
        clothes_name, clothes_type = map(str, input().split())
        dict[clothes_type] += 1
    ans = 1
    for i in clothes_type.keys():
        ans *= dict[i] + 1
    print(ans - 1)