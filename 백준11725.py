import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline
N = int(input())
graph = [[0]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)
ans = list()
def dfs(v):
    visited[v] = 1
    for i in range(1, N+1):
        if(visited[i] == 0 and graph[v][i] == 1):
            ans.append([v, i])
            dfs(i)