import sys


sys.setrecursionlimit(100000)
input = sys.stdin.readline

#y, x
M, N, K = map(int, input().split())
paper = [[0]*N for _ in range(M)]
visited = [[0]*N for _ in range(M)]
ans = list()
count = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(xpos, ypos):
    global count
    for i in range(4):
        current_x = xpos + dx[i]
        current_y = ypos + dy[i]
        if 0<=current_x<M and 0<=current_y<N and visited[current_x][current_y] == 0 and paper[current_x][current_y] == 0:
            visited[current_x][current_y] = 1
            count += 1
            dfs(current_x, current_y)
    return


for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            paper[j][i] = 1
            
for i in range(M):
    for j in range(N):
        if paper[i][j] == 0 and visited[i][j] == 0:
            visited[i][j] = 1
            count += 1
            dfs(i,j)
            ans.append(count)
        count=0
ans.sort()
print(len(ans))
for i in ans:
    print(i, end=' ')
            