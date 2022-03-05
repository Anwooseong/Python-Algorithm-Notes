n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
result = []
count = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(graph, xpos, ypos):
    queue = []
    queue.append([xpos, ypos])
    graph[xpos][ypos] = 0
    value = 1

    while queue:
        current = queue.pop(0)
        current_x = current[0]
        current_y = current[1]
        for i in range(0, 4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if(0 <= next_x < n and 0 <= next_y < n):
                if(graph[next_x][next_y] == 1):
                    queue.append([next_x, next_y])
                    value += 1
                    graph[next_x][next_y] = 0
    return value

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(graph, i, j))
            count += 1
result.sort()
print(count)
for i in range(len(result)):
    print(result[i])