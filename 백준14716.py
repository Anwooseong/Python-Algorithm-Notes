import sys


input = sys.stdin.readline
M, N = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(M))
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(xpos, ypos):
    queue = list()
    queue.append([xpos, ypos])
    while queue:
        current_x, current_y = queue.pop(0)
        for i in range(8):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if 0<=next_x<M and 0<= next_y<N and graph[next_x][next_y] == 1:
                graph[next_x][next_y] = 3
                queue.append([next_x, next_y])


count = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i, j)
            count += 1
print(count)