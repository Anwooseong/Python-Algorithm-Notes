import sys


input = sys.stdin.readline
N = int(input())
time_list = list()
for _ in range(N):
    time_list.append(list(map(int, input().split())))
time_list.sort(key=lambda x:x[0])
time_list.sort(key=lambda x:x[1])
count = 1
finish_time = time_list[0][1]
for i in range(1, N):
    if time_list[i][0] >= finish_time:
        finish_time = time_list[i][1]
        count += 1
print(count)