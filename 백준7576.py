from collections import deque
import sys


input = sys.stdin.readline
M, N = map(int, input().split())
graph = list(list(map(int, input().split()))for _ in range(N))
queue = deque()
visited = [[False]*M for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        current_x, current_y= queue.popleft()
        visited[current_x][current_y] = True
        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if 0<=next_x<N and 0<=next_y<M and graph[next_x][next_y] == 0 and visited[next_x][next_y] == False:
                graph[next_x][next_y] = graph[current_x][current_y] + 1
                queue.append([next_x, next_y])

bfs()
flag = False
max_count = 0
for i in graph:
    for j in i:
        if j == 0:
            flag = True
            break
        max_count = max(max_count, j)
if flag:
    print(-1)
elif max_count == 1:
    print(0)
else:
    print(max_count-1)