import sys
sys.setrecursionlimit(1000000)


input = sys.stdin.readline
N = int(input())
area = [list(map(int, input().split()))for _ in range(N)]
max_count = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(xpos, ypos, height):
    for i in range(4):
        current_x = xpos + dx[i]
        current_y = ypos + dy[i]
        if 0<=current_x<N and 0<=current_y<N and visited[current_x][current_y]==0 and area[current_x][current_y]>height:
            visited[current_x][current_y] = 1
            dfs(current_x, current_y, height)


for height in range(max(map(max, area)),-1,-1):
    visited = [[0]*N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if height < area[i][j] and visited[i][j] == 0:
                visited[i][j] = 1
                count += 1
                dfs(i, j, height)
    max_count = max(max_count, count)
print(max_count)