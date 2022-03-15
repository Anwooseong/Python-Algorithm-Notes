import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
graph = [[0]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)
#ans = list()

def dfs(v):
    #visited[v] = 1
    for i in range(2, N+1):
        if v == 1 and graph[v][i] == 1: #v가 1이면 그때의 i는 무조건 자식
            #ans.append([v,i])#[부모, 자식]
            visited[i] = v ################
            dfs(i)
        else:
            if visited[i] == 0 and graph[v][i] == 1: #i인덱스에 방문을 하지않았다. 즉 v가 부모라는 뜻
                #ans.append([v, i])
                visited[i] = v ##############
                dfs(i)
    return
            
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    
visited[1]=1 ###############
dfs(1)
for i in range(2, N+1): #############
    print(visited[i])  ################
#ans.sort(key=lambda x:x[1]) #자식작은순으로 정렬
#for i in range(len(ans)):
    #print(ans[i][0])