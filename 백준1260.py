def dfs(start_node):
    visited_dfs[start_node] = 1
    print(start_node, end=' ')
    for i in graph[start_node]:
        if visited_dfs[i] == 0:
            dfs(i)

def bfs(start_node):
    visited_bfs[start_node] = 1
    result_bfs = []
    queue = []
    queue.append(start_node)
    while queue:
        current = queue.pop(0)
        result_bfs.append(current)
        for i in graph[current]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = 1
    return result_bfs


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited_dfs = [0]*(N + 1)
visited_bfs = [0]*(N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(N + 1):
    graph[i].sort()

dfs(V)

print()
ans_bfs = bfs(V)
for i in range(len(ans_bfs)):
    print(ans_bfs[i], end= ' ')