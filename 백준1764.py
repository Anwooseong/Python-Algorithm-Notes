N, M = map(int, input().split())
set_A = set()
set_B = set()
for _ in range(N):
    set_A.add(input())
for _ in range(M):
    set_B.add(input())
ans = sorted(set_A & set_B)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])