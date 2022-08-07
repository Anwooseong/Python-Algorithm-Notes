
from collections import deque
import sys

#벽 3개를 설치하는 것 구현하기
input = sys.stdin.readline
N, M = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(N))
visited = [[False]*M for _ in range(N)]
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            queue.append([i, j])

def bfs(xpos, ypos):
    while queue:
        current_x, current_y = queue.popleft()
        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if 0<=next_x<N and 0<=next_y<M:
                if graph[next_x][next_y] == 0:
                    queue.append([next_x, next_y])
                    graph[next_x][next_y] = 2
                    visited[next_x][next_y] = True

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            visited[i][j] = True
            bfs(i, j)
count = 0
print('--------------')
for i in range(N):
    for j in range(M):
        print(graph[i][j], end=' ')
        if graph[i][j] == 2:
            count+=1
    print()

print(count)