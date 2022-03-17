import sys


input = sys.stdin.readline
T = int(input())

def bfs(xpos, ypos):
    queue = list()
    queue.append([xpos, ypos])
    while queue:
        current = queue.pop(0)
        current_x = current[0]
        current_y = current[1]
        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if 0<=next_x<N and 0<=next_y<M and area[next_x][next_y] == 1:
                area[next_x][next_y] = 0
                queue.append([next_x, next_y])

for _ in range(T):
    M, N, K = map(int, input().split())
    area = [[0]*M for _ in range(N)]

    for _ in range(K):
        y, x = map(int, input().split())
        area[x][y] = 1

    count = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]


    for i in range(N):
        for j in range(M):
            if area[i][j] == 1:
                bfs(i,j)
                count+=1
    print(count)
