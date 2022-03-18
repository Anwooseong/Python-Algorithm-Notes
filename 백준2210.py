import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
graph = list(list(map(str, input().split())) for _ in range(5))
result = set()
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(xpos, ypos, arr):
    if len(arr) == 6:
        result.add(arr)
        return
    for i in range(4):
        next_x = xpos + dx[i]
        next_y = ypos + dy[i]
        if 0<=next_x<5 and 0<=next_y<5:
            dfs_arr = arr + graph[next_x][next_y]
            dfs(next_x, next_y, dfs_arr)
 

for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])
    
print(len(result))
