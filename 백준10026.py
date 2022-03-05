def nomal_bfs(graph, xpos, ypos):
    nomal_visited[xpos][ypos] = 1
    result = graph[xpos][ypos]
    queue = []
    queue.append([xpos, ypos])
    while queue:
        current = queue.pop(0)
        current_x = current[0]
        current_y = current[1]
        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N:
                if graph[next_x][next_y] == result and nomal_visited[next_x][next_y]== 0:
                    queue.append([next_x, next_y])
                    nomal_visited[next_x][next_y] = 1


def bfs(graph, xpos, ypos):
    visited[xpos][ypos] = 1
    if graph[xpos][ypos] in ['R', 'G']:
        result = ['R', 'G']
    else:
        result = ['B']
    queue = []
    queue.append([xpos, ypos])
    while queue:
        current = queue.pop(0)
        current_x = current[0]
        current_y = current[1]
        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N:
                if graph[next_x][next_y] in result and visited[next_x][next_y] == 0:
                    queue.append([next_x, next_y])
                    visited[next_x][next_y] = 1

N = int(input())
graph = []
first_count = 0
second_count = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(N):
    graph.append(list(map(str, input())))

nomal_visited = [[0]*N for _ in range(N)]
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if nomal_visited[i][j] == 0:
            nomal_bfs(graph, i, j)
            first_count += 1
        if visited[i][j] == 0:
            bfs(graph, i ,j)
            second_count += 1
print(first_count, end=' ')
print(second_count)
