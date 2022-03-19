import sys


input = sys.stdin.readline
N, M, K = map(int, input().split())
graph = [[0]*M for _ in range(N)]
queue = list()
visited = [[False]*M for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(K):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

def bfs(xpos, ypos):
    queue.append([xpos, ypos])
    visited[xpos][ypos] = True
    count = 1
    while queue:
        current = queue.pop(0)
        current_x = current[0]
        current_y = current[1]
        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if 0<=next_x<N and 0<=next_y<M and graph[next_x][next_y]==1:
                if visited[next_x][next_y] == False:
                    graph[next_x][next_y] = 0
                    visited[next_x][next_y] = True
                    queue.append([next_x, next_y])
                    count+=1
    return count

max_count = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            bfs_count = bfs(i,j)
            max_count = max(max_count, bfs_count)
print(max_count)
            
