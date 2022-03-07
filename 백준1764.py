N, M = map(int, input().split())
set_A = set()
set_B = set()
for _ in range(N):
    set_A.add(input())
for _ in range(M):
    set_B.add(input())
result = sorted(list(set_A & set_B))
for i in range(len(result)):
    print(result[i])