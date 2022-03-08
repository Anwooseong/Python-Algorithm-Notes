N, M = map(int, input().split())
result = dict()
for i in range(N):
    home_page, password = map(str, input().split())
    result[home_page] = password
for i  in range(M):
    print(result[input()])