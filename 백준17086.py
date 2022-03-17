import sys

input = sys.stdin.readline
N, M = map(int, input().split())
area = list()
for _ in range(N):
    area.append(list(map(int, input().split())))
queue = list()
for i in range(N):
    for j in range(M):
        if area[i][j] == 1:
            queue.append([i, j])
dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,-1,1,-1,1]

def bfs():
    while queue:

        current = queue.pop(0)
        current_x = current[0]
        current_y = current[1]

        for i in range(8):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if 0<=next_x<N and 0<=next_y<M and area[next_x][next_y] == 0:
                area[next_x][next_y] = area[current_x][current_y] + 1
                queue.append([next_x, next_y])
    return

bfs()
print(max(map(max, area))-1)