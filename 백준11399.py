N = int(input())
time = list(map(int, input().split()))
time.sort()
add_time = 0
ans = 0
for i in range(N):
    add_time = add_time + time[i]
    ans += add_time
print(ans)